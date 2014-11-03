var labsControllers = angular.module('labsApp.controllers',['ui.router',]);

labsControllers.controller('TweetCtrl',function TweetCtrl($scope, $state, Tweet, AuthUser){
	$scope.tweets = {};
  $scope.authuser = AuthUser.username;
  


	var tweets = Tweet.query(function(){
		$scope.tweets = tweets;
	});

   $scope.deleteTweet = function(tweet) {   
     if (tweet.user != $scope.authuser){
      alert('다른 사용자의 트윗은 삭제할 수 없습니다.');
     }
     else{
     tweet.$delete({id:tweet.id});
     idx = $scope.tweets.indexOf(tweet);
     $scope.tweets.splice(idx,1);
     };
   };

	$scope.submitTweet = function(text){
	   	var tweet = new Tweet({text : text });
		tweet.$save(function(){
			$scope.tweets.unshift(tweet);
		})
	};
});

labsControllers.controller('QCtrl',function ($scope,HelloWorld) {
    alert('alert');
   //alert(HelloWorld.getMessages());
   $scope.messages = HelloWorld.getMessages();
});


// labsControllers.controller('UserCtrl',function ($scope, $state, Tweet, User, AuthUser){

// 	$scope.tweets = {};
//     $scope.user = {}
// 	var tweets = User.get({id : AuthUser.id}, function(){
// 		$scope.tweets = tweets.tweets;
//         $scope.user = tweets;
// 	});

// });
labsControllers.controller('UserCtrl', function ($scope, $stateParams, Tweet, User, AuthUser) {
  $scope.tweets = {};
  console.log($stateParams);
  console.log('para: '||$stateParams.userId);
  id = AuthUser.id;

   var resp = function(response){
    $scope.user = response;
    $scope.tweets = response.tweets;
  };
  

  if (id == '') {    
    User.get(resp);
  }
  else
  {
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

labsControllers.controller('LEDCtrl', function($scope, $http, $state, djangoForm){
  $scope.submit = function(){
    $http.post("led/", $scope.led_data).success(function(out_data){
      if (!djangoForm.setErrors($scope.LEDForm, out_data.errors)){
        var canvas = document.getElementById("myCanvas");
        var context = canvas.getContext('2d');
        
       // alert(out_data.hexRGB);
        context.strokeStyle = "#0000ff";
        context.rect(0,0 , 30, 130 );
        context.closePath() 
        context.fillStyle = out_data.hexRGB;
        context.fill();
        context.stroke();
      }
      }).error(function(){
        console.error('LED Error');
      })
    };
});

labsControllers.controller('TemperatureCtrl', function(){
   null;
});

labsControllers.controller('HomeCtrl', function($state,$stateParams){
  // console.log($state.current.data.customData1);
  // console.log($state.current.data.customData2);
  null;
});

labsControllers.controller('TodoCtrl', function($scope, Todo){
  $scope.todos = {}
  
  var todos = Todo.query(function(){
    $scope.todos = todos;
  });

  $scope.add = function(message){
    var $error = $("#error");  
    var $todoText = $("#todoText");  

    if (message == null){    
      $error.text("Error");
      // $error.toggleClass('ng-hide');
      $error.removeClass('ng-hide');
      $error.addClass('ng-show');
      return;
    }else{
      // $error.toggleClass('ng-hide');
      $error.removeClass('ng-show');
      $error.addClass('ng-hide');

      var todo = new Todo({message : message});
      todo.$save();
      $scope.todos.push(todo);
      $scope.message =' ';
    };    

  };

  $scope.done = function(todo){
    todo.$delete({id : todo.id});
    var idx = $scope.todos.indexOf(todo);    
    $scope.todos.splice(idx, 1);
  }

});

labsControllers.controller('BoardCtrl',function($state, $scope, $stateParams, Board, Post, Reply){
  $scope.board= {};
  $scope.posts = {}
  var id = $stateParams.id;
  console.log('a : ' + $stateParams.id);

  var board = Board.get({id:id}, function(response){
    $scope.board = response;
  });

  var posts = Board.get({id:id}, function(response){
    $scope.posts = response.posts;
  });
})

labsControllers.controller('MenuCtrl', function($scope, $stateParams, BoardList){
  var boards = BoardList.query(function(response){
    $scope.boards = boards;
  });
})