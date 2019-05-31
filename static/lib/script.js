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
            housingRule($scope.state)
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
class Alarm {
    constructor(iconElem) {
        this.icon = $(iconElem);
        this.loop = false;
        this.enabled = false;
    }
    enable() {
        this.enabled = true;
        this.icon.css('opacity', 1)
        this.runAnimation();
    }
    runAnimation() {
        if (this.enabled) {
            var next = {}
            if (this.loop) {
                var a = this;
                next.complete = function () {
                    a.runAnimation();
                }
            }
            this.icon
                .fadeOut()
                .fadeIn(next);
        }
    }
    disable() {
        if (this.enabled) {
            this.enabled = false;
            this.icon.finish()
                .css('opacity', 0);
        }
    }
}
alarms = {}
alarms.tcs = new Alarm('#icon-tc-idle')
alarms.housing = new Alarm('#icon-housing')
alarms.sheep = new Alarm('#icon-sheep')

alarms.tcs.loop = true;