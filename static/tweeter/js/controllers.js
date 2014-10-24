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

// labsControllers.controller('UserCtrl',function ($scope, $state, Tweet, User, AuthUser){

// 	$scope.tweets = {};
//     $scope.user = {}
// 	var tweets = User.get({id : AuthUser.id}, function(){
// 		$scope.tweets = tweets.tweets;
//         $scope.user = tweets;
// 	});

// });
labsControllers.controller('UserCtrl', function ($scope, Tweet, User, AuthUser) {
  $scope.tweets = {};
  id = AuthUser.id;

  console.log('userctrl');
  console.log(id);

   var resp = function(response){
    $scope.user = response;
    $scope.tweets = response.tweets;
  };
  

  if (id == '') {
  
    console.log('a');
    User.get(resp);
  }
  else
  {
    console.log('b');
     User.get({id:id}, resp);
    };


  // User.get({id:id}, function(response) {
  //   $scope.user = response;
  //   $scope.tweets = response.tweets;
  // });

  $scope.submitTweet = function(text){
        var tweet = new Tweet({text : text });
        tweet.$save(function(){
            $scope.tweets.unshift(tweet);
        })
    };

});

// labsControllers.controller('ProfileCtrl',function ($http, $window){
//     $window.location.href = 'profile/1';
//     // $http.get("profile/", AuthUser.id).success(function(out_data){
//     //     $scope.user = out_data;
// });

// 사용자 등록 화면에서 사용할 controller
labsControllers.controller('RegisterCtrl',function ( $scope, $http,$state, $window, djangoForm){
       // sumbit버튼을 Click했을 때 호출될 function
	   $scope.submit = function() {
        if ($scope.subscribe_data) {
            // $http.post resouce를 이용하여 form에서 작성한 값을 post방식으로 view에 전달함. 
            // 성공하면 .success call back function을 호출하여 view에서 return한 값을 이용함.
            $http.post("register/", $scope.subscribe_data).success(function(out_data) {
                // 아래 jangoForm.setErrors는 화면에 Validation결과를 뿌려줌. 
                if (!djangoForm.setErrors($scope.RegForm, out_data.errors)) {
                   // $state resource를 이용하여 성공시 페이지 이동. 
                   // go의 변수에 해당하는 값이 app.js의 router에 구성이 되어 있어야 함. 
                    $state.go(out_data.success_url);
                }
            }).error(function() {
                console.error('An error occured during submission');
            })
        };
    };
});

labsControllers.controller('SuccessRegisterCtrl', function ($scope, $http){
    $scope.first = 'frist';
    $scope.target ='ddd';
    })

// djangoForm이 있어야 Valiation한 결과가 Web화면에 보여짐. 
labsControllers.controller('LoginCtrl', function ($scope, $http, $state, $window, djangoForm){
    $scope.submit = function(){
        $http.post("login/", $scope.login_data).success(function(out_data){       
            if (!djangoForm.setErrors($scope.LoginForm, out_data.errors)){ 
                                                                            
                                $window.location.href = out_data.success_url;
                                
                                // $state.go(out_data.success_url); // 정상적으로 처리가 되면 view에서 정의한 Success_url로 redirect
                }
            }).error(function(){
                console.error('An error occured during submission');
            })
        };
});






