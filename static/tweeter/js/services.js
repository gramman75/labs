angular.module('labsApp.services',['ngResource'])
	.factory('Tweet', function($resource){
		return $resource('/api/tweets/:id/');
	})
	.factory('User', function($resource){
		return $resource('/api/users/:id/');
	})

