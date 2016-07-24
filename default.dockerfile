FROM ubuntu:14.04.4

## local variables
ENV ROOT_PROJECT /var/machine-learning
ENV ENVIRONMENT docker
ENV ENVIRONMENT_DIR $ROOT_PROJECT/puppet/environment/$ENVIRONMENT

## copy files into container
RUN mkdir /var/machine-learning
COPY . /var/machine-learning

## install git, and wget
#
#  Note: r10k requires 'git' installed
RUN apt-get -y update
RUN apt-get -y install git=1:1.9.1-1ubuntu0.3
RUN apt-get -y install wget=1.15-1ubuntu1.14.04.2

## install puppet
RUN wget https://apt.puppetlabs.com/puppetlabs-release-pc1-trusty.deb
RUN dpkg -i puppetlabs-release-pc1-trusty.deb
RUN apt-get -y update
RUN apt-get -y install puppet-agent

## install r10k
RUN apt-get -y install rubygems-integration=1.5
RUN gem install r10k -v 2.2.0

## install puppet modules using puppetfile with r10k
RUN mkdir -p $ENVIRONMENT_DIR/modules_contrib/
RUN PUPPETFILE=$ROOT_PROJECT/test/Puppetfile PUPPETFILE_DIR=$ENVIRONMENT_DIR/modules_contrib/ r10k puppetfile install

## provision with puppet
RUN /opt/puppetlabs/bin/puppet apply $ENVIRONMENT_DIR/manifests/install_packages.pp --modulepath=$ENVIRONMENT_DIR/modules_contrib:$ENVIRONMENT_DIR/modules --confdir=$ROOT_PROJECT/test
RUN /opt/puppetlabs/bin/puppet apply $ENVIRONMENT_DIR/manifests/install_sklearn.pp --modulepath=$ENVIRONMENT_DIR/modules_contrib:$ENVIRONMENT_DIR/modules --confdir=$ROOT_PROJECT/test
RUN /opt/puppetlabs/bin/puppet apply $ENVIRONMENT_DIR/manifests/configure_system.pp --modulepath=$ENVIRONMENT_DIR/modules_contrib:$ENVIRONMENT_DIR/modules --confdir=$ROOT_PROJECT/test
RUN /opt/puppetlabs/bin/puppet apply $ENVIRONMENT_DIR/manifests/compile_asset.pp --modulepath=$ENVIRONMENT_DIR/modules_contrib:$ENVIRONMENT_DIR/modules --confdir=$ROOT_PROJECT/test

## show directory
RUN ls -l $ROOT_PROJECT/interface/static/js
RUN ls -l $ROOT_PROJECT/interface/static/css
RUN ls -l $ROOT_PROJECT/interface/static/img
