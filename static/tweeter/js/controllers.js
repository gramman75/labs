var labsControllers = angular.module('labsApp.controllers',['ui.router',]);

labsControllers.controller('TweetCtrl',function TweetCtrl($scope, $state, Tweet){
	$scope.tweets = {};

	var tweets = Tweet.query(function(){
		$scope.tweets = tweets;
	});

	$scope.submitTweet = function(text){
		var tweet = new Tweet({text : text });
		tweet.$save(function(){
			$scope.tweets.unshift(tweet);
		})
	};
});

labsControllers.controller('UserCtrl',function ($scope, $state, Tweet, User, AuthUser){
   


	$scope.tweets = {};


	var tweets = User.get({id : AuthUser.id}, function(){
		$scope.tweets = tweets.tweets;
        $scope.user = tweets.user;
	});

});

labsControllers.controller('RegisterCtrl',function ( $scope, $http,$state, $window, djangoForm){

       

	   $scope.submit = function() {
        if ($scope.subscribe_data) {
            $http.post("register/", $scope.subscribe_data).success(function(out_data) {
            	// $state.go('success_register');	
                if (!djangoForm.setErrors($scope.RegForm, out_data.errors)) {
                    // on successful post, redirect onto success page
                     // $window.location.href = '/success_register/';
                    // return $resource('/success_register/');
                    $state.go(out_data.success_url);
                    // $state.go('^.sibling')
                }
            }).error(function() {
                console.error('An error occured during submission');
            })
        };
    };
});

// djangoForm이 있어야 Valiation한 결과가 Web화면에 보여짐. 
labsControllers.controller('SuccessRegisterCtrl', function ($scope, $http){
    $scope.first = 'frist';
    $scope.target ='ddd';
    })

labsControllers.controller('LoginCtrl', function ($scope, $http, $state, djangoForm){
    $scope.submit = function(){
        $http.post("login/", $scope.login_data).success(function(out_data){       
            if (!djangoForm.setErrors($scope.LoginForm, out_data.errors)){                                    
                                $state.go(out_data.success_url); // 정상적으로 처리가 되면 view에서 정의한 Success_url로 redirect
                }
            }).error(function(){
                console.error('An error occured during submission');
            })
        };
});






