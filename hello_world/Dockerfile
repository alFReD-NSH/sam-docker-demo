FROM public.ecr.aws/lambda/python:3.9 as build

# Look it up here https://omahaproxy.appspot.com/
ARG chrome_branch_base_position=1097615

ARG chromedriver_version=111.0.5563.64

RUN yum install -y unzip && \
    curl -Lo "/tmp/chromedriver.zip" "https://chromedriver.storage.googleapis.com/$chromedriver_version/chromedriver_linux64.zip" && \
    curl -Lo "/tmp/chrome-linux.zip" "https://www.googleapis.com/download/storage/v1/b/chromium-browser-snapshots/o/Linux_x64%2F$chrome_branch_base_position%2Fchrome-linux.zip?alt=media" && \
    unzip /tmp/chromedriver.zip -d /opt/ && \
    unzip /tmp/chrome-linux.zip -d /opt/

FROM public.ecr.aws/lambda/python:3.9
RUN yum install atk cups-libs gtk3 libXcomposite alsa-lib \
    libXcursor libXdamage libXext libXi libXrandr libXScrnSaver \
    libXtst pango at-spi2-atk libXt xorg-x11-server-Xvfb \
    xorg-x11-xauth dbus-glib dbus-glib-devel -y
COPY --from=build /opt/chrome-linux /opt/chrome
COPY --from=build /opt/chromedriver /opt/

COPY requirements.txt .

RUN pip install -r requirements.txt -t .

COPY . .

# Command can be overwritten by providing a different command in the template directly.
CMD ["app.lambda_handler"]
