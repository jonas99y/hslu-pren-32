SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
export PYTHONPATH="${SCRIPT_DIR}/src/"
eval python3 "${SCRIPT_DIR}/src/app.py"