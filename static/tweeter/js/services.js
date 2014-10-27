angular.module('labsApp.services',['ngResource'])
	.factory('Tweet', function($resource){
		return $resource('/api/tweets/:id/');
	})
	.factory('User', function($resource){
		return $resource('/api/users/:id/');
	})
	.factory('HelloWorld', function($q, $timeout) {
  
    var getMessages = function() {
      var deferred = $q.defer();
  
      $timeout(function() {
        deferred.resolve(['Hello', 'world']);
      }, 0);
  
      return deferred.promise;
    };
    
    return {
      getMessages: getMessages
    };
  
  })