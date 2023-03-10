#!/bin/bash

echo "DIRNAME: ${dirname}"

if [ -d "expressjs/views/homepage/node_modules" ]
then
    # cd expressjs/views/homepage && node run build
    (cd expressjs/views/homepage; npm run start)  # "frontend" w/ create-react-app way
    # (npm start)  # "backend" w/ some typescript & expressjs thing i started out messing with
else
    echo "Cant run!  need to run 'npm install' first (o_o)"
fi

