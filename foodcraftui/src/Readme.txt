Instructions:
After git pull
1. npm install in the directory which has package.json
2. ng serve in the same directory.(it will look for angulr-cli.json file)
3. if you face error like ng is not recognized, then install - > npm install -g @angular/cli
4. Now use  ng serve .It should serve application on localhost:4200 and takes you to localhost:4200/course

To change endpoint url

Go to src -> app -> register-course and open register-course.service.ts
you will see a variable called -> resourceUrl. change its value accordingly.



