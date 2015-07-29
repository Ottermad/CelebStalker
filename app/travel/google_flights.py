flights_request = '''{{
  "request": {{
    "passengers": {{
      "adultCount": {},
      "childCount": {},
      "seniorCount": {}
    }},
    "slice": [
      {{
        "origin": "{}",
        "destination": "{}",
        "date": "{}",
	"preferredCabin": "COACH"
      }}
    ],
    "saleCountry": "{}"
  }}
}}
'''
