FROM mongo

COPY teachers.json /teachers.json

CMD mongoimport --host mongodb --db singlestone --collection teachers --type json --file /teachers.json --jsonArray