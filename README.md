# OnlineMarketPlace
OnlineMarketPlace with Django

## Installation

1. Clone the repository:
   git clone https://github.com/OrroZorro/OnlineMarketPlace.git
   
2.Create and activate a virtual environment
(on macOS):
  python3 -m venv venv
  source venv/bin/activate
(on Windows)
  py -m venv venv
  venv\Scripts\activate

3.Download dependencies
  pip install -r requirements.txt

4.Perform database migrations:
(macOS)
  python3 manage.py migrate
(Windows)
  py manage.py migrate

5.Create a `.env` file in the project root directory and add the following variables:
  SECRET_KEY=your secret key
  DEBUG=True

6. cd puddle
(macOS)
   python3 manage.py runserver
(Windows)
  py manage.py runserver
