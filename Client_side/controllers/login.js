
app.controller('login', function ($scope, services,$state)
 {

    $scope.login = function(){
     console.log('login');
     var user = {
        username : $scope.username,
        password : $scope.password
     }
     console.log(user);
     services.loginUser(user).then(
        function success(response) {
          //response.data=
          console.log("successful login");
          // location.replace("dashboard");
          //location.replace("http://127.0.0.1:8000/accounts/login/chat/");
          //$state.go("http://127.0.0.1:8000/chat/");
          console.log(response);
          console.log(response.user);
           $state.go("http://127.0.0.1:8000/accounts/login/chat/");
        },
        function error(response) {
          console.log("unsuccessful login");
          console.log(response);
          console.log(response.data);  
        },
      );
    }
 })



 
