/*************************************************************************
 *purpose   : controller is responsible for accepting and sending data.
 * @file    : registration.js
 * @author  : Pushkar
 * @version : 1.0
 * @since   : 22/01/2019 
 **********************************************************************/
// app.controller('registrationctrl', function ($scope,userservices)
//app.controller('registrationctrl', function ($scope,services, $state)
app.controller('registration', function ($scope,services, $state)
 {  
     $scope.registration = function() {
     console.log('registration');
     var user = {
         username: $scope.username,
         email:$scope.email,
         password:$scope.password
     }
     console.log(user);
     services.registerUser(user).then(
         function successCallback(response){
             console.log("registration sucessful");
             console.log(response.user);
             //user.save();
             $state.go("login");
         },
         function errorCallback(response){
             console.log("register unsuccessful");
             console.log(response.user)
         }
     );
    // services.registerUser(user);
    }
    
 });


 
 


 
 
