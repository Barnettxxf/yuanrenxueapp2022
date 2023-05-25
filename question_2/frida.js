Java.perform(() => {
    const ChallengeTwoFragment = Java.use('com.yuanrenxue.match2022.fragment.challenge.ChallengeTwoFragment');
    console.log('ChallengeTwoFragment:', ChallengeTwoFragment)
    const sign = ChallengeTwoFragment.sign;
    sign.implementation = function (a) {
        console.log('params:', a)
        const result = this.sign(a)
        console.log('result:', result)
        return result;
    };
});