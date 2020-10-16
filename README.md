# scrapy_flask_facebook
scrapy_flask_facebook is an advanced crawler for Facebook, written in python, based on the [Scrapy](https://scrapy.org/) framework. 

python scrapyapp.py

## Post example

URL : http://localhost:8083/scrape
```python
Body:

{
  "facebook_profile": "zappos"
}

Response :
{
  "awards": [
    "#31 - Fortune Magazine 100 Best Companies to Work For"
  ], 
  "categories": [
    "Clothes shop"
  ], 
  "company_address": "400 Stewart Ave", 
  "company_address1": "Las Vegas, NV, US", 
  "company_overview": " offers free shipping and free return shipping with a 365-day return policy. Choose from over 1000 brands, over 100,000 styles, and over 3 million items from our warehouse full of shoes, clothing, handbags, and accessories!", 
  "email": "cs@zappos.com", 
  "founding_date": "Founded in 1999", 
  "image": "https://scontent.fvga4-1.fna.fbcdn.net/v/t1.0-1/p720x720/121366000_10157318797012687_4333303292555202638_o.jpg?_nc_cat=1&_nc_sid=dbb9e7&_nc_ohc=kQVGqav2bOgAX9RvDz-&_nc_ht=scontent.fvga4-1.fna&tp=6&oh=8b9d945c4dec67e3f246f2b68f15861b&oe=5FB04D94", 
  "milestones": null, 
  "mission": "We are a service company that happens to sell shoes, clothes, and more.", 
  "office_hours": null, 
  "products": "#31 - Fortune Magazine 100 Best Companies to Work For", 
  "url": "https://www.facebook.com/zappos/about/", 
  "weburl": null
}
```