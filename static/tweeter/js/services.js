angular.module('labsApp.services',['ngResource'])
	.factory('Tweet', function($resource){
		return $resource('/api/tweets/:id/');
	})
	.factory('User', function($resource){
		return $resource('/api/users/:id/');
	})
  .factory('Todo', function($resource){
    return $resource('/api/todos/:id/');
  })
  .factory('Post', function($resource){
    return $resource('/api/posts/');
  })
  .factory('Board', function($resource){
    return $resource('/api/boards/:id/');
  })
  .factory('Reply', function($resource){
    return $resource('/api/replies/:id/');
  })
  .factory('BoardList',function($resource){
    return $resource('/api/boardList/:id/');
  })
  .factory('SamSkill', function($resource){
    return $resource('api/samskills/');
  })
  .factory('SamEmployee',function($resource){
    return $resource('api/samemployees/');
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
