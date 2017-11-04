main:
	hugo server --buildDrafts

dev: dev-no-tidy tidy

dev-no-tidy:
	- rm -r public
	hugo --buildDrafts --baseUrl https://conferences.sigcomm.org/imc/2017/dev/
	find public -name .DS_Store -delete

tidy:
	- find public -name *.html -print -exec tidy -modify -indent -quiet --tidy-mark no {} \;

dev-live:
	- rm -r public
	hugo --baseUrl https://conferences.sigcomm.org/imc/2017/dev/
	find public -name .DS_Store -delete
	- find public -name *.html -exec tidy -modify -indent -quiet --tidy-mark no {} +

live:
	rm -r public
	hugo
	find public -name .DS_Store -delete
	- find public -name *.html -exec tidy -modify -indent -quiet --tidy-mark no {} +
