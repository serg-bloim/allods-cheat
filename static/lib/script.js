var app = angular.module('BlankApp', ['ngMaterial', 'ngMessages']);
app.controller("myCtrl", ($scope, $http, $mdDialog) => {
    $scope.updateInterval = 1000;
    $scope.changeUpdateInterval = setUpdateInterval;
    $scope.url = 'game'
    $scope.dbg = true
    $scope['alarms'] = alarms;
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
    $scope.muted=false;
    $scope.muteAll=function(ev){
        $scope.muted = !$scope.muted;
        $('audio').each(function(i,elem){
            elem.muted=$scope.muted;
        })
    }
}).filter('icon', function(){
    return function(input, type){
        var id = input
        if(_.isPlainObject(input)){
            type = ['', 'unit', 'building', 'tech'][input['kind']];
            id = input['iconId']
        }
        return 'static/icon/'+type+'_icon_'+(id.toString().padStart(3,'0'))+'.png'
    }
});
function setUpdateInterval() {
    console.log('setUpdateInterval')
    clearInterval(this.timerId)
    this.timerId = setInterval(this.update, this.updateInterval)
    this.update()
}
// app.filter('floor', Math.floor);
app.filter('floor', () => { return Math.floor });
class Alarm {
    constructor(name, iconElem, soundElemId, soundUrl, repeat) {
        this.name = name;
        this.id = '#icon-'+name;
        this.icon = $(iconElem);
        this.snd = $(soundElemId)[0];
        this.loop = true;
        this.enabled = false;
        if(repeat === undefined){
            repeat=false;
        }
        this.repeat = repeat;
        this.muted = false;
        this.soundUrl = soundUrl;
        this.volume = 1;
        this.init_loop=this.loop;
    }
    enable() {
        if (!this.enabled || this.repeat) {
            this.enabled = true;
            var elem = $(this.id)
            elem.css('opacity', 1)
            this.runAnimation(elem);
            this.snd = $('#snd-'+this.name)[0];
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
    runAnimation(elem) {
        if (this.enabled) {
            var next = {}
            if (this.loop) {
                var a = this;
                next.complete = function () {
                    a.runAnimation(elem);
                }
            }
            elem
                .fadeOut()
                .fadeIn(next);
        }
    }
    disable() {
        if (this.enabled) {
            this.enabled = false;
            var elem = $(this.id)
            elem.finish()
                .css('opacity', 0);
            this.snd = $('#snd-'+this.name)[0];
            this.snd.pause();
        }
    }
}
alarms = {}

alarms.tcs = new Alarm('tc-idle', '#icon-tc-idle', '#snd_almost_idle_tc', 'static/audio/bell-cut.mp3', true)
alarms.housing = new Alarm('housing','#icon-housing', '#snd_housing', 'static/audio/train-cut.mp3')
alarms.sheep = new Alarm('sheep', '#icon-sheep', '#sound4', 'static/audio/bell-cut.mp3')

alarms.tcs.loop = true;