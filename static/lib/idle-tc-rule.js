function idleTCRule(tcs) {
    var anyCloseIdle = false;
    var anyIdle = false;
    tcs.forEach(tc => {
        _.merge(tc, { flags: {} });
        if (isTcIdle(tc)) {
            tc.flags.color = 'red';
            anyIdle = true;
        } else if (isTcCloseToIdle(tc)) {
            tc.flags.color = 'orange';
            anyCloseIdle = true;
        }
    });
    var sndIdle = document.getElementById('snd_idle_tc');
    var sndAlmostIdle = document.getElementById('snd_almost_idle_tc');
    if (anyIdle || anyCloseIdle) {
        alarms.tcs.enable();
    } else {
        // sndAlmostIdle.pause();
        alarms.tcs.disable();
    }
}

function isTcIdle(tc) {
    return tc.queue.length == 0;
}
function isTcCloseToIdle(tc) {
    return tc.prodProgress >= 0.85 && tc.queue.length == 1;
}

function play(audio) {
    audio.play().then(_ => {
        // Automatic playback started!
        // Show playing UI.
    })
        .catch(error => {
            // Auto-play was prevented
            // Show paused UI.
        });
}