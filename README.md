# PyLock

PyLock is a Python project that demonstrates the use of locks for achieving mutual exclusion. It is inspired by the concepts discussed in "Operating Systems Three Easy Pieces" by Andrea Arpaci-Dusseau and Remzi Arpaci-Dusseau.

## Description

The PyLock project showcases the implementation of mutual exclusion using locks in Python. It provides a simple script that utilizes locks to ensure that shared data is accessed by threads in a controlled and synchronized manner.

## Features

-   Utilizes the `threading` module in Python for multi-threading
-   Implements locks to provide mutual exclusion
-   Supports modification of shared data by multiple threads concurrently
-   Demonstrates the use of the `with` statement for acquiring and releasing locks

## Requirements

-   Python 3.x

## Usage

1. Clone the repository:

git clone https://github.com/your-username/pylock.git

2. Navigate to the project directory:

cd pylock

3. Run the script:

python pylock.py

4. The script will execute and demonstrate the mutual exclusion behavior using locks. The shared data modifications will be printed to the console.

## Contributing

Contributions to PyLock are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
