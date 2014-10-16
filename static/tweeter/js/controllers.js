var tweeterControllers = angular.module('tweeterApp.controllers',['ui.router',]);

tweeterControllers.controller('TweetCtrl',function TweetCtrl($scope, Tweet){
	$scope.tweets = {};

	var tweets = Tweet.query(function(){
		$scope.tweets = tweets;
	});

	$scope.submitTweet = function(text){
		var tweet = new Tweet({text : text });
		tweet.$save(function(){
			$scope.tweets.unshift(tweet);
		})
	}

});

tweeterControllers.controller('UserCtrl',function ($scope, Tweet, User, AuthUser){
	$scope.tweets = {};

	var tweets = User.get({id : AuthUser.id}, function(){
		$scope.tweets = tweets.tweets;
	});

});

tweeterControllers.controller('RegisterCtrl',function ( $scope, $http,$state, $window, djangoForm){
     	

	   $scope.submit = function() {
        if ($scope.subscribe_data) {
            $http.post("register/", $scope.subscribe_data).success(function(out_data) {
            		
                if (!djangoForm.setErrors($scope.my_form, out_data.errors)) {
                    // on successful post, redirect onto success page
                    // $window.location.href = out_data.success_url;
                    // return $resource('/success_register/');
                    $state.go('success_register');
                }
            }).error(function() {
                console.error('An error occured during submission');
            });
        }
        return false;
    };
});

