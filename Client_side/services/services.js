app.service('services', function ($http, $location) {

  /**
   * @description define registerUser() function to register user and passing user data as an argument
   * @param user data
   */
  this.registerUser = function(user) {
      /**
       * declaring $http variable and returning to get an instance after $http service
       * to make rest API calls
       */
     return $http({
          //declaring method type
          method: 'POST',
          //calling register API call
           url: 'http://127.0.0.1:8000/',
        //url: 'login',
          //sending user register data
          data: user
      })
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
        //  url: 'http://localhost:8000/login',
         url: 'http://127.0.0.1:8000/accounts/login/chat/',
        // url: 'http://127.0.0.1:8000/chat/',
         //sending user register data
         data: user
     })
 }
});