#!/bin/sh
cd frontend/
npm run build
npm run generate
aws s3 cp dist/ s3://www.buserlab.com --recursive