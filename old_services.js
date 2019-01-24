// app.service('userservices', function ($http) {
app.service('services', function ($http, $location) {
    this.registerUser = function (user) {
      $http({
        method: 'POST',//issues a post request top the following url
        url: 'http://localhost:3000/registration',
        data: user
      }).then(
        function sucess(response) {
          console.log("successful registration");
          console.log(response);
          console.log(response.data);
  
        },
        function error(response) {
  
          console.log("unsuccessful registration");
          console.log(response);
          console.log(response.data);
  
        },

        this.loginUser = function (user) {
          /**
           * declaring $http variable and returning to get an instance after $http service
           * to make rest API calls
           */
         return $http({
              //declaring method type
              method: 'POST',
              //calling register API call
              url: 'http://localhost:8000/login',
              //sending user register data
              data: user
          })
        })
    }});
