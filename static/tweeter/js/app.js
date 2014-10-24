angular.module('labsApp', [
  'ui.router',
  'ngResource',
  'labsApp.services',
  'labsApp.controllers',
  'ng.django.forms',
])
  .config(function ($interpolateProvider, $httpProvider, $resourceProvider, $stateProvider, $urlRouterProvider) {
    // Force angular to use square brackets for template tag
    // The alternative is using {% verbatim %}
    $interpolateProvider.startSymbol('[[').endSymbol(']]');

    // CSRF Support
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
    $httpProvider.defaults.headers.common['X-CSRFToken'] = '{% csrf_value %}';

    // This only works in angular 3!
    // It makes dealing with Django slashes at the end of everything easier.
    $resourceProvider.defaults.stripTrailingSlashes = false;

    // Django expects jQuery like headers
    // $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8';

    // Routing

    $urlRouterProvider.otherwise('/');
    $stateProvider
      .state('home',{
        url : '/',
        templateUrl : 'static/common/partials/home.html',
        controller : 'HomeCtrl',
      })
      .state('tweets', {
        url: '/tweets',
        templateUrl: 'static/tweeter/partials/tweet-list.html',
        controller: 'TweetCtrl',
      })
      .state('my-tweets', {
        url: '/users/:userId/',
        templateUrl: 'static/tweeter/partials/tweet-list.html',
        controller: 'UserCtrl',
      })
      .state('profile', {
        url: '/profile/:userId/',
        templateUrl: 'static/common/partials/profile.html',
        controller: 'UserCtrl',
      })
      // .state('profile', {
      //   url : '/profile/:user_id/',
      //   templateUrl : '/profile/1',
      //   controller : 'ProfileCtrl',
      // })
      // form을 이용할 경우의 state구문. template은 django template dir에 있어야 함. 
       .state('register',{
        url : '/register/',        
        templateUrl : 'register/',
        controller : 'RegisterCtrl',
       })
       // django template을 이용하지 않고 angular로 구성이 되는 페이지. template은 partials에 있음.
       .state('success_register',{
        url : '/success_register/',
        templateUrl : 'static/common/partials/success_register.html',
        controller : 'SuccessRegisterCtrl',
       })
       .state('login',{
        url : '/login/',
        templateUrl : 'login/',
        controller : 'LoginCtrl',
       })
  });

// angular.module('tweeterApp',[
// 	'ui.router',
// 	'ngResource',
// 	'tweeterApp.controllers',
// 	'tweeterApp,services'
// 	])
// 	.config(function( $interpolateProvider , $stateProvider, $urlRouterProvider,$resourceProvider){
// 		$interpolateProvider.startSymbol('[[').endSymbol(']]');

// 		$resourceProvider.defaults.stripTrailingSlashes = false;

// 		$urlRouterProvider.otherwise('/');
		
// 		$stateProvider
// 			.state('tweets',{
// 				url : '/:id',
// 				templateUrl : 'static/tweeter/partials/tweet-list.html',
// 				controller : 'TweetCtrl',
// 			})
// 			.state('my-tweets',{
// 				url : '/:userId',
// 				templateUrl : 'static/tweeter/partials/tweet-list.html',
// 				controller : 'UserCtrl',

// 			})
// 	});