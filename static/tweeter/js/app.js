angular.module('tweeterApp', [
  'ui.router',
  'ngResource',
  'tweeterApp.services',
  'tweeterApp.controllers',
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
      .state('tweets', {
        url: '/:id',
        templateUrl: 'static/tweeter/partials/tweet-list.html',
        controller: 'TweetCtrl',
      })
      .state('my-tweets', {
        url: '/:userId',
        templateUrl: 'static/tweeter/partials/tweet-list.html',
        controller: 'UserCtrl',
      })
      .state('profile', {
        url: '/profile/:userId',
        templateUrl: 'static/tweeter/partials/profile.html',
        controller: 'UserCtrl',
      })
       .state('register',{
        url : '/register/',        
        templateUrl : 'register/',
        controller : 'RegisterCtrl',
       })
       .state('success_register',{
        url : 'success_register',
        templateUrl : 'static/common/partials/success_register.html',
        controller : 'SuccessRegisterCtrl',
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