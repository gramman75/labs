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

tweeterControllers.controller('RegisterCtrl',function ($scope, $http, djangoForm){
    

	$scope.submit = function(){	

		var in_data = { username : $scope.username,
						password : $scope.password,
						confirm  : $scope.confirm,
						email	 : $scope.email,
						firstname : $scope.firstname,
						lastname  : $scope.lastname,
						hobby     : $scope.hobby };
		
	if ($scope.password != $scope.confirm) {
			alert('패스워드 다시 입력');
		};	

	$http.post('register/',in_data)
		.success(function(out_data){
			alert(out_data);				
			});	
	};
})

