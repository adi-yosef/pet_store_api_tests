* clone this repo
* run commands to open venv:
    * windows: 
        python -m venv venv
        venv\Scripts\activate
    * mac/linux:
        python3 -m venv venv
        source venv/bin/activate

* run this command to install requirements:
    * pip install -r requirements.txt

* run this command to install playwright browsers drivers:
    * playwright install


run commands:
* pytest : runs all tests
* pytest -v -s : runs all tests with verbose and prints
* pytest -k <expression>: runs test with test name as string exp. pytest -v -s -k "test_find_pet_by_status_available" 
* pytest -v -s -m <mark>: runs all tests with pytest mark exp. pytest -v -s -m "smoke"  




