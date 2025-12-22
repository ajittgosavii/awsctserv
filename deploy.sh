#!/bin/bash
# AWS Enterprise Assessment Platform - Deployment Script
# Usage: ./deploy.sh [local|docker|aws]

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
APP_NAME="aws-assessment-platform"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

print_header() {
    echo -e "${BLUE}"
    echo "╔══════════════════════════════════════════════════════════╗"
    echo "║     AWS Enterprise Assessment Platform - Deployment      ║"
    echo "╚══════════════════════════════════════════════════════════╝"
    echo -e "${NC}"
}

print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠ $1${NC}"
}

print_error() {
    echo -e "${RED}✗ $1${NC}"
}

check_prerequisites() {
    echo -e "${BLUE}Checking prerequisites...${NC}"
    
    # Check Python
    if command -v python3 &> /dev/null; then
        PYTHON_VERSION=$(python3 --version)
        print_success "Python found: $PYTHON_VERSION"
    else
        print_error "Python 3 not found. Please install Python 3.9+"
        exit 1
    fi
    
    # Check pip
    if command -v pip3 &> /dev/null; then
        print_success "pip found"
    else
        print_error "pip not found"
        exit 1
    fi
}

check_docker() {
    if command -v docker &> /dev/null; then
        print_success "Docker found"
        return 0
    else
        print_error "Docker not found"
        return 1
    fi
}

check_aws_cli() {
    if command -v aws &> /dev/null; then
        print_success "AWS CLI found"
        return 0
    else
        print_warning "AWS CLI not found"
        return 1
    fi
}

deploy_local() {
    echo -e "\n${BLUE}Deploying locally...${NC}\n"
    
    check_prerequisites
    
    # Create virtual environment if not exists
    if [ ! -d "venv" ]; then
        echo "Creating virtual environment..."
        python3 -m venv venv
        print_success "Virtual environment created"
    fi
    
    # Activate virtual environment
    source venv/bin/activate
    
    # Install dependencies
    echo "Installing dependencies..."
    pip install -r requirements.txt -q
    print_success "Dependencies installed"
    
    # Check for API key
    if [ -z "$ANTHROPIC_API_KEY" ]; then
        print_warning "ANTHROPIC_API_KEY not set. AI features will be disabled."
        echo "Set with: export ANTHROPIC_API_KEY=your-key-here"
    else
        print_success "ANTHROPIC_API_KEY configured"
    fi
    
    echo -e "\n${GREEN}Starting application...${NC}\n"
    streamlit run streamlit_app.py
}

deploy_docker() {
    echo -e "\n${BLUE}Deploying with Docker...${NC}\n"
    
    if ! check_docker; then
        print_error "Docker is required for this deployment method"
        exit 1
    fi
    
    # Check for API key
    if [ -z "$ANTHROPIC_API_KEY" ]; then
        print_warning "ANTHROPIC_API_KEY not set"
        read -p "Enter your Anthropic API key: " ANTHROPIC_API_KEY
        export ANTHROPIC_API_KEY
    fi
    
    # Build image
    echo "Building Docker image..."
    docker build -t ${APP_NAME}:latest .
    print_success "Docker image built"
    
    # Run container
    echo "Starting container..."
    docker run -d \
        --name ${APP_NAME} \
        -p 8501:8501 \
        -e ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY} \
        ${APP_NAME}:latest
    
    print_success "Container started"
    echo -e "\n${GREEN}Application available at: http://localhost:8501${NC}\n"
}

deploy_docker_compose() {
    echo -e "\n${BLUE}Deploying with Docker Compose...${NC}\n"
    
    if ! check_docker; then
        print_error "Docker is required"
        exit 1
    fi
    
    if ! command -v docker-compose &> /dev/null && ! docker compose version &> /dev/null; then
        print_error "Docker Compose not found"
        exit 1
    fi
    
    # Check for API key
    if [ -z "$ANTHROPIC_API_KEY" ]; then
        print_warning "ANTHROPIC_API_KEY not set"
        read -p "Enter your Anthropic API key: " ANTHROPIC_API_KEY
        export ANTHROPIC_API_KEY
    fi
    
    # Deploy with compose
    if docker compose version &> /dev/null; then
        docker compose up -d --build
    else
        docker-compose up -d --build
    fi
    
    print_success "Services started"
    echo -e "\n${GREEN}Application available at: http://localhost:8501${NC}\n"
}

deploy_aws() {
    echo -e "\n${BLUE}Deploying to AWS...${NC}\n"
    
    if ! check_aws_cli; then
        print_error "AWS CLI is required for AWS deployment"
        exit 1
    fi
    
    if ! check_docker; then
        print_error "Docker is required for building container images"
        exit 1
    fi
    
    # Get AWS account info
    ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text 2>/dev/null)
    if [ -z "$ACCOUNT_ID" ]; then
        print_error "Could not get AWS account ID. Please configure AWS credentials."
        exit 1
    fi
    print_success "AWS Account: $ACCOUNT_ID"
    
    REGION=${AWS_REGION:-$(aws configure get region)}
    if [ -z "$REGION" ]; then
        REGION="us-east-1"
    fi
    print_success "AWS Region: $REGION"
    
    STACK_NAME="${APP_NAME}-stack"
    ECR_REPO="${APP_NAME}-app"
    
    echo -e "\n${BLUE}Step 1: Deploy CloudFormation stack...${NC}"
    
    # Check if stack exists
    if aws cloudformation describe-stacks --stack-name $STACK_NAME &> /dev/null; then
        print_warning "Stack exists, updating..."
        aws cloudformation update-stack \
            --stack-name $STACK_NAME \
            --template-body file://cloudformation-template.yaml \
            --capabilities CAPABILITY_NAMED_IAM \
            --parameters ParameterKey=Environment,ParameterValue=production 2>/dev/null || true
    else
        echo "Creating new stack..."
        aws cloudformation create-stack \
            --stack-name $STACK_NAME \
            --template-body file://cloudformation-template.yaml \
            --capabilities CAPABILITY_NAMED_IAM \
            --parameters ParameterKey=Environment,ParameterValue=production
    fi
    
    echo "Waiting for stack to be ready..."
    aws cloudformation wait stack-create-complete --stack-name $STACK_NAME 2>/dev/null || \
    aws cloudformation wait stack-update-complete --stack-name $STACK_NAME 2>/dev/null || true
    
    print_success "CloudFormation stack ready"
    
    echo -e "\n${BLUE}Step 2: Build and push Docker image...${NC}"
    
    # Login to ECR
    aws ecr get-login-password --region $REGION | docker login --username AWS --password-stdin ${ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com
    
    # Build image
    docker build -t ${ECR_REPO}:latest .
    
    # Tag and push
    docker tag ${ECR_REPO}:latest ${ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com/${ECR_REPO}:latest
    docker push ${ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com/${ECR_REPO}:latest
    
    print_success "Image pushed to ECR"
    
    echo -e "\n${BLUE}Step 3: Update ECS service...${NC}"
    
    # Force new deployment
    CLUSTER_NAME=$(aws cloudformation describe-stacks --stack-name $STACK_NAME --query "Stacks[0].Outputs[?OutputKey=='ECSClusterName'].OutputValue" --output text)
    aws ecs update-service --cluster $CLUSTER_NAME --service ${STACK_NAME}-service --force-new-deployment --no-cli-pager
    
    print_success "ECS service updated"
    
    # Get application URL
    APP_URL=$(aws cloudformation describe-stacks --stack-name $STACK_NAME --query "Stacks[0].Outputs[?OutputKey=='ApplicationURL'].OutputValue" --output text)
    
    echo -e "\n${GREEN}═══════════════════════════════════════════════════════════${NC}"
    echo -e "${GREEN}Deployment complete!${NC}"
    echo -e "${GREEN}Application URL: ${APP_URL}${NC}"
    echo -e "${GREEN}═══════════════════════════════════════════════════════════${NC}\n"
    
    print_warning "Don't forget to update the Anthropic API key in Secrets Manager!"
}

cleanup() {
    echo -e "\n${BLUE}Cleaning up...${NC}"
    
    # Stop Docker containers
    if docker ps -q --filter "name=${APP_NAME}" | grep -q .; then
        docker stop ${APP_NAME} 2>/dev/null || true
        docker rm ${APP_NAME} 2>/dev/null || true
        print_success "Containers stopped"
    fi
    
    # Remove Docker image
    docker rmi ${APP_NAME}:latest 2>/dev/null || true
    
    print_success "Cleanup complete"
}

show_help() {
    print_header
    echo "Usage: ./deploy.sh [COMMAND]"
    echo ""
    echo "Commands:"
    echo "  local         Deploy locally with virtual environment"
    echo "  docker        Deploy with Docker"
    echo "  compose       Deploy with Docker Compose"
    echo "  aws           Deploy to AWS ECS Fargate"
    echo "  cleanup       Stop and remove containers"
    echo "  help          Show this help message"
    echo ""
    echo "Environment Variables:"
    echo "  ANTHROPIC_API_KEY    API key for Claude AI features"
    echo "  AWS_REGION           AWS region for deployment"
    echo ""
    echo "Examples:"
    echo "  ./deploy.sh local"
    echo "  ANTHROPIC_API_KEY=sk-xxx ./deploy.sh docker"
    echo "  ./deploy.sh aws"
}

# Main
print_header

case "${1:-help}" in
    local)
        deploy_local
        ;;
    docker)
        deploy_docker
        ;;
    compose)
        deploy_docker_compose
        ;;
    aws)
        deploy_aws
        ;;
    cleanup)
        cleanup
        ;;
    help|*)
        show_help
        ;;
esac
