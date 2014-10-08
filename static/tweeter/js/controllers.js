var tweeterControllers = angular.module('tweeterApp.controllers',[]);

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

tweeterControllers.controller('RegisterCtrl',function ($scope, $http){
	$scope.username = 'test';
	$scope.password  ='pw';

	$scope.submit = function(){
		var in_data = { username : $scope.username };		
		$http.post('register/',in_data)
			.success(function(out_data){
				alert(out_data);
			});
	};
})

