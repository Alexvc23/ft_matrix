#!/bin/bash

# Define color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Print message to indicate the start of the configuration process
echo -e "${GREEN}Configuring the project...${NC}"

# Step 1: Check if the virtual environment already exists
if [[ -d "myenv" ]]; then
    # If the "myenv" directory exists, skip the creation step
    echo -e "${YELLOW}Virtual environment already exists. Skipping creation...${NC}"
else
    # If the "myenv" directory does not exist, create a virtual environment
    echo -e "${GREEN}Creating a virtual environment...${NC}"
    python3 -m venv myenv
fi

# Step 2: Activate the virtual environment
# The "source" command activates the virtual environment, enabling its usage
echo -e "${GREEN}Activating the virtual environment...${NC}"
source myenv/bin/activate

# Step 3: Check for requirements.txt and existing packages
# Verify if the requirements.txt file exists
echo -e "${GREEN}Checking for requirements.txt file...${NC}"
if [[ -f "requirements.txt" ]]; then
    echo -e "${GREEN}requirements.txt found. Checking for installed packages...${NC}"
    # List currently installed packages in the virtual environment and save to a temporary file
    pip freeze > current_packages.txt
    # Compare the current packages with the required ones in requirements.txt
    if cmp -s requirements.txt current_packages.txt; then
        # If the files match, no additional installation is needed
        echo -e "${YELLOW}All required packages are already installed. Skipping installation...${NC}"
    else
        # If the files do not match, install missing dependencies
        echo -e "${GREEN}Installing missing dependencies...${NC}"
        pip install -r requirements.txt
    fi
    # Remove the temporary file after the comparison
    rm current_packages.txt
else
    # Exit with an error if requirements.txt is not found
    echo -e "${RED}requirements.txt not found. Please provide a requirements.txt file to install dependencies.${NC}"
    exit 1
fi

# Step 4: Confirm setup success
# Final message indicating the completion of the configuration process
echo -e "${GREEN}Project configuration complete! Activate your virtual environment using 'source myenv/bin/activate' and run your scripts.${NC}"
