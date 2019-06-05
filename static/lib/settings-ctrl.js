function SettingsCtrl($scope, $mdDialog) {
    $scope.save = function () {
        dialog.close($scope.item);
    };

    $scope.close = function () {
        $mdDialog.hide();
    };

    $scope.updateVolume = function (name, opt) {
        snd = document.getElementById('snd_'+name);
        snd[opt] = $scope.settings.snd[name][opt];
    };

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