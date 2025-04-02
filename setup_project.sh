#!/bin/bash
# Script to create a Python virtual environment and install dependencies

# Colors and formatting
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[0;33m'
RED='\033[0;31m'
BOLD='\033[1m'
NC='\033[0m' # No Color

# Icons
CHECK="✅"
INFO="ℹ️ "
WARN="⚠️ "
PACKAGE="📦"
WRENCH="🔧"
ROCKET="🚀"

# Name of the virtual environment directory
ENV_DIR="env"

echo -e "${BLUE}${INFO} ${BOLD}Starting Python environment setup...${NC}"

# Check if virtual environment directory already exists and is valid
if [ -d "$ENV_DIR" ] && [ -f "$ENV_DIR/bin/activate" ]; then
    echo -e "${BLUE}${INFO} Virtual environment '$ENV_DIR' already exists.${NC}"
else
    # Remove existing directory if it exists but is invalid
    if [ -d "$ENV_DIR" ]; then
        echo -e "${YELLOW}${WARN} Found incomplete virtual environment. Removing it...${NC}"
        rm -rf "$ENV_DIR"
    fi
    
    echo -e "${BLUE}${INFO} Creating virtual environment in '$ENV_DIR'...${NC}"
    python3 -m venv "$ENV_DIR"
    echo -e "${GREEN}${CHECK} Virtual environment created.${NC}"
fi

# Activate the virtual environment
echo -e "${BLUE}${INFO} Activating virtual environment...${NC}"
source "$ENV_DIR/bin/activate"
echo -e "${GREEN}${CHECK} Virtual environment activated.${NC}"

# Install or update dependencies if requirements.txt exists
if [ -f "requirements.txt" ]; then
    echo -e "${BLUE}${INFO} Checking and installing dependencies from requirements.txt...${NC}"
    pip install -r requirements.txt --upgrade
    
    # Alternative method to install missing packages
    echo -e "${BLUE}${INFO} Installing any missing packages...${NC}"
    pip list --format=freeze > installed.txt && grep -v -f installed.txt requirements.txt | xargs -r pip install
    
    # Verify all packages are installed
    while IFS= read -r package || [ -n "$package" ]; do
        # Skip empty lines and comments
        [[ $package =~ ^[[:space:]]*$ || $package =~ ^#.*$ ]] && continue
        
        # Extract package name without version
        pkg_name=$(echo "$package" | cut -d'=' -f1 | cut -d'>' -f1 | cut -d'<' -f1 | tr -d ' ')
        
        if ! pip show "$pkg_name" >/dev/null 2>&1; then
            echo -e "${BLUE}${PACKAGE} Installing missing package: $pkg_name${NC}"
            pip install "$package"
        fi
    done < requirements.txt
    echo -e "${GREEN}${CHECK} All dependencies installed successfully.${NC}"
else
    echo -e "${YELLOW}${WARN} No requirements.txt file found. Skipping dependency installation.${NC}"
fi

# Create alias
echo -e "${BLUE}${WRENCH} Creating norminette alias for flake8...${NC}"
alias norminette=flake8

# Determine which shell configuration file to use
if [ -n "$ZSH_VERSION" ]; then
    SHELL_CONFIG="$HOME/.zshrc"
elif [ -n "$BASH_VERSION" ]; then
    SHELL_CONFIG="$HOME/.bashrc"
else
    SHELL_CONFIG="$HOME/.profile"
fi

# Add aliases to shell config if not already there
for alias_cmd in "alias norminette=flake8" "alias py=python3" "alias pt=python -m pytest -W ignore::DeprecationWarning"; do
    if [ -f "$SHELL_CONFIG" ] && grep -q "$alias_cmd" "$SHELL_CONFIG"; then
        echo -e "${BLUE}${INFO} Alias '${alias_cmd#alias }' already exists in $SHELL_CONFIG${NC}"
    else
        echo -e "${BLUE}${INFO} Adding alias '${alias_cmd#alias }' to $SHELL_CONFIG for persistence...${NC}"
        echo "$alias_cmd" >> "$SHELL_CONFIG"
        echo -e "${GREEN}${CHECK} Alias added.${NC}"
    fi
done

source "$SHELL_CONFIG"

echo -e "${BLUE}${INFO} Aliases added to $SHELL_CONFIG. To use them in this session, run: source $SHELL_CONFIG${NC}"

echo -e "${GREEN}${ROCKET} ${BOLD}Setup complete!${NC}"
echo ""
echo -e "${BLUE}${INFO} To activate the virtual environment in the future, run:${NC}"
echo -e "${BOLD}   source $ENV_DIR/bin/activate${NC}"
echo -e "${BLUE}${INFO} The norminette alias is active for this session. Use 'norminette file.py' to run flake8.${NC}"