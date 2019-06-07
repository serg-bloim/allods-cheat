function SettingsCtrl($scope, $mdDialog) {
    $scope.save = function () {
        dialog.close($scope.item);
    };

    $scope.close = function () {
        $mdDialog.hide();
    };

    $scope.updateVolume = function (alarm, opt) {
        var snd = $('#snd-'+alarm.name)[0];
        snd[opt] = alarm[opt];
    };
    var snds =
        [
            'bell-cut.mp3',
            'ice-cubes.mp3',
            'ring-cut.mp3',
            'sound1.wav',
            'sound2.wav',
            'train-cut.mp3',
            'whistle-cut.mp3'
        ];

    $scope.sounds=_.map(snds,
        function(snd){
            return { label: snd, url: '/static/audio/' + snd };
        });

    // $scope.saveClose = function () {
    //     $scope.settings = $scope.changed;
    //     for (name in $scope.settings.snd) {
    //         snd = document.getElementById('snd_'+name);
    //         sndSetting = $scope.settings.snd[name];
    //         for (opt in sndSetting) {
    //             snd[opt] = sndSetting[opt];
    //         }
    //     }
    //     $mdDialog.hide();
    // };
}