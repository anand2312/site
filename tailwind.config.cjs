module.exports = {
	content: ['./src/**/*.{html,js,svelte,ts}'],
	theme: {
		fontFamily: {
			display: ['JetBrains Mono', 'monospace'],
			body: ['JetBrains Mono', 'monospace']
		},
		extend: {
			colors: {
				pink: {
					50: '#F2D7EE',
					500: '#DE4D86'
				},
				dblue: {
					500: '#0E103D'
				},
				gold: {
					100: '#F4D35E'
				},
				lgreen: {
					100: '#2CA58D'
				}
			}
		}
	},
	plugins: []
};
