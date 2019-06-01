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
            housing: {
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
    $scope.reset = function(ev){
        $http.get('reset')
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
    constructor(iconElem, soundElemId, repeat) {
        this.icon = $(iconElem);
        this.snd = $(soundElemId)[0];
        this.loop = true;
        this.enabled = false;
        if(repeat === undefined){
            repeat=false;
        }
        this.repeat = repeat;
    }
    enable() {
        if (!this.enabled || this.repeat) {
            this.enabled = true;
            this.icon.css('opacity', 1)
            this.runAnimation();
            this.snd.play().then(_ => {
                // Automatic playback started!
                // Show playing UI.
              })
              .catch(error => {
                // Auto-play was prevented
                // Show paused UI.
              });;
        }
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
            this.snd.pause();
        }
    }
}
alarms = {}

alarms.tcs = new Alarm('#icon-tc-idle', '#snd_almost_idle_tc', true)
alarms.housing = new Alarm('#icon-housing', '#snd_housing')
alarms.sheep = new Alarm('#icon-sheep', '#sound4')

alarms.tcs.loop = true;