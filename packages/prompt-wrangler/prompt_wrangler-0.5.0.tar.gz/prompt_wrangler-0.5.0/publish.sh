#!/bin/bash

# Run tests
echo "Running tests..."
pytest
test_result=$?

if [ $test_result -eq 0 ]; then
    # Extract the previous version number from setup.py
    previous_version=$(grep 'version=' setup.py | cut -d '"' -f 2)

    # Print the previous version number
    echo "Previous version number: $previous_version"

    # Prompt for the new version number
    echo "Enter the new version number (e.g., 0.1.1):"
    read new_version

    # Update the version number in setup.py
    sed -i.bak "s/version=\"[^\"]*\"/version=\"$new_version\"/g" setup.py
    rm setup.py.bak

    # Remove any previous distribution files
    rm -rf dist/*

    # Create a source distribution and a wheel distribution
    python setup.py sdist bdist_wheel

    # Upload the package to PyPI
    twine upload dist/*
else
    echo "Tests failed. Fix the issues before publishing."
fi
