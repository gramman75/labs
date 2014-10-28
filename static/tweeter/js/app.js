// var interceptor = function ($q, $location) {
//     return {
//         request: function (config) {
//             console.log(config);
//             return config;
//         },

//         response: function (result) {
//             console.log('Repos:');
//             result.data.splice(0, 10).forEach(function (repo) {
//                 console.log(repo.name);
//             })
//             return result;
//         },

//         responseError: function (rejection) {
//             console.log('Failed with', rejection.status, 'status');
//             if (rejection.status == 500) {              
//                 $location.url('/');
//             }

//             return $q.reject(rejection);
//         }
//     }
// };

angular.module('labsApp', [
  'ui.router',
  'ngResource',
  'labsApp.services',
  'labsApp.controllers',
  'ng.django.forms',
])
  .config(function ($interpolateProvider, $httpProvider, $resourceProvider, $stateProvider, $urlRouterProvider) {
    // http intercept

//     $httpProvider.interceptors.push(
//       function ($q, $location) {
//         return {
//           request: function (config) {
//                      console.log(config['url']);
//                      return config;
//                    },
//           // response: function (result) {
//           //             console.log('Repos:');
//           //             result.data.splice(0, 10).forEach(function (repo) {
//           //                                                 console.log(repo.name);
//           //                                               })
//           //             return result;
//           //           },

//           responseError: function (rejection) {
//                            console.log('Failed with', rejection.status, 'status');
//                            if (rejection.status == 500) {              
//                               console.log(rejection.statusText);
//                                 // $state.go('home');
//                                window.location = "#/"
//                               // $scope.$apply(function() { $location.path("/"); });
//                                // $location.path('/index.html');
//                            }
//                           return $q.reject(rejection);
//                         }
//                }
//       }
// );
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
    //alert(MyRoute);
    $urlRouterProvider.otherwise('/');
    $stateProvider
      .state('home',{
        url : '/',
        templateUrl : 'static/templates/common/home.html',
        controller : 'HomeCtrl',
        //data : {customData1 : 1, customData2 : 'abc'}, // Controller에 Data 전달 
      })
      .state('tweets', {
        url: '/tweets',
        templateUrl: 'static/templates/tweeter/tweet-list.html',
        controller: 'TweetCtrl',
      })
      .state('my-tweets', {
        url: '/users/:userId',
        templateUrl: 'static/templates/tweeter/tweet-list.html',
        controller: 'UserCtrl',
      })
      .state('profile', {
        url: '/profile/:userId',
        templateUrl: 'static/templates/common/profile.html',
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
        templateUrl : 'static/templates/common/success_register.html',
        controller : 'SuccessRegisterCtrl',
       })
       .state('login',{
        url : '/login/',
        templateUrl : 'login/',
        controller : 'LoginCtrl',
       })
       .state('led', {
        url : '/led/',
        templateUrl : 'led/',
        controller : 'LEDCtrl',
       })
       .state('temperature', {
        url : '/temperature/',
        templateUrl : 'temperature/',
        controller : 'TemperatureCtrl',
       })
       .state('q',{
        url : '/q',
        templateUrl : 'static/templates/common/q.html',
        controller : 'QCtrl',
       })
  });