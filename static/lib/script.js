var app = angular.module('BlankApp', ['ngMaterial', 'ngMessages']);
app.controller("myCtrl", ($scope, $http, $mdDialog) => {
    $scope.updateInterval = 1000;
    $scope.changeUpdateInterval = setUpdateInterval;
    $scope.url = 'game'
    $scope.dbg = true
    $scope.settings = {
        snd: {
            almost_idle_tc: {
                volume: 1,
                loop: true
            },
            idle_tc: {
                volume: 1,
                loop: true
            },
        }
    }

    $scope.update = () => {
        $scope.url = 'game' + ($scope.dbg ? '-dbg' : '');
        $http.get($scope.url).then((resp) => {
            $scope.state = resp.data
            idleTCRule($scope.state.tcs)
        })
    }
    $scope.changeUpdateInterval();
    $scope.openSettings = function (ev) {
        $mdDialog.show({
            controller: SettingsCtrl,
            clickOutsideToClose: true,
            parent: angular.element(document.body),
            targetEvent: ev,
            scope: $scope,
            preserveScope: true,
            templateUrl: 'static/tpl/settings.html',
            fullscreen: $scope.customFullscreen // Only for -xs, -sm 
        });
    }
})
function setUpdateInterval() {
    console.log('setUpdateInterval')
    clearInterval(this.timerId)
    this.timerId = setInterval(this.update, this.updateInterval)
    this.update()
}
// app.filter('floor', Math.floor);
app.filter('floor', () => { return Math.floor });