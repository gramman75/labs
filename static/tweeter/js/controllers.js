var tweeterControllers = angular.module('tweeterApp.controllers',['ui.router',]);

tweeterControllers.controller('TweetCtrl',function TweetCtrl($scope, $state, Tweet){
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

    $scope.submit = function(){
        $state.go('profile');
    }

});

tweeterControllers.controller('UserCtrl',function ($scope, $state, Tweet, User, AuthUser){
    


	$scope.tweets = {};


	var tweets = User.get({id : AuthUser.id}, function(){
		$scope.tweets = tweets.tweets;
        $scope.user = tweets.user;
	});

});

tweeterControllers.controller('RegisterCtrl',function ( $scope, $http,$state, $window, djangoForm){

       

	   $scope.submit = function() {
        if ($scope.subscribe_data) {
            $http.post("register/", $scope.subscribe_data).success(function(out_data) {
            	// $state.go('success_register');	
                if (!djangoForm.setErrors($scope.my_form, out_data.errors)) {
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


// tweeterControllers.controller('RegisterCtrl',function ( $scope, $http,$state){
//     $scope.submit = function() {
//         $state.go('success_register');
//     }
// });


tweeterControllers.controller('SuccessRegisterCtrl', function ($scope){
    $scope.first = 'frist';
    $scope.target ='ddd';
    })






