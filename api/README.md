# Quotes API

This is a simple Python / Flask powered API for web development purposes.

This application is CORS enabled, so all endpoints are open to public consumption. There is no security on the endponts.

The quotes api itself does support proper HTTP verb endpoints. You should be able to do the following actions:

## API

     /api/quote/          | GET    | returns all quotes
     /api/quote/{id}      | GET    | returns a specific quote by 'id'
     /api/quote/          | POST   | add a new quote
     /api/quote/          | PUT    | update an quote
     /api/quote/{id}      | DELETE | deletes an quote
     
## Usage Notes

You will need to have Python 3.6 and Flask installed for
 this application to run correctly.  
 
 The start up file for the API is `app.py`. 
 
 To install `Flask` for this application use the command:
 
 `pip install -U flask`

  To install `CORS` for this application use the command:
  
 `pip install -U flask-cors`    