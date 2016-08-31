# Machine Learning [![Build Status](https://travis-ci.org/jeff1evesque/machine-learning.svg?branch=master)](https://travis-ci.org/jeff1evesque/machine-learning)

In [machine learning](http://en.wikipedia.org/wiki/Machine_learning), support
vector machines (SVMs) are [supervised learning](http://en.wikipedia.org/wiki/
Supervised_learning) models with associated learning [algorithms](http://en.wi
kipedia.org/wiki/Algorithm) that analyze data and recognize patterns, used for
 [classification](http://en.wikipedia.org/wiki/Statistical_classification) and
 [regression analysis](http://en.wikipedia.org/wiki/Regression_analysis).  More
 generally, machine-learning deals with the construction and study of systems
 that can [learn](http://en.wikipedia.org/wiki/Learning) from data, rather than
 follow only explicitly programmed instructions.

Applications for machine learning include:

- [Object recognition](http://en.wikipedia.org/wiki/Object_recognition)
- [Natural language processing](http://en.wikipedia.org/wiki/Natural_language_processing)
- [Search engines](http://en.wikipedia.org/wiki/Search_engines)
- [Bioinformatics](http://en.wikipedia.org/wiki/Bioinformatics)
- [Stock market](http://en.wikipedia.org/wiki/Stock_market) analysis
- [Speech](http://en.wikipedia.org/wiki/Speech_recognition) and [handwriting recognition](http://en.wikipedia.org/wiki/Speech_recognition)
- [Sentiment analysis](http://en.wikipedia.org/wiki/Sentiment_analysis)
- [Recommender systems](http://en.wikipedia.org/wiki/Recommender_system)
- [Sequence mining](http://en.wikipedia.org/wiki/Sequence_mining), commonly
 referred as *data mining*
- [Computational advertising](http://en.wikipedia.org/wiki/Computational_advertising)
- [Computational finance](http://en.wikipedia.org/wiki/Computational_finance)

## Support [![paypal](https://camo.githubusercontent.com/11b2f47d7b4af17ef3a803f57c37de3ac82ac039/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f70617970616c2d646f6e6174652d79656c6c6f772e737667)](https://www.paypal.me/jeff1evesque) [![bitcoin](https://camo.githubusercontent.com/c705adb6695b3d8f60b9a005674cb58b3f1ef1cc/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f646f6e6174652d626974636f696e2d677265656e2e737667)](http://coinbase.com/jeff1evesque)

Donations are very appreciated.  Smaller donations, could fund a latté, during
 a late night meddling code.  While larger donations, could fund further
 research, by assisting the cost for the following:

- server(s): this could be made open to the public, and implementing machine-
learning.
- peripheral device(s): these device(s) could connect to the machine-learning
 server(s):
  - [raspberry pi](https://www.raspberrypi.org/): these devices could
 communicate to the machine-learning server(s), or *peripheral device(s)*.
  - [xbee chip](www.digi.com/lp/xbee): these chips could implement the
 [zigbee](http://www.zigbee.org/) wireless protocol, allowing peripheral
 device(s) to transmit data between one another, and finally to the machine-
 learning server(s).
  - [sensor](http://www.adafruit.com/categories/35): multiple types of sensors
 could be connected via the [zigbee](http://www.zigbee.org/) wireless protocol
 to other sensor(s), raspberry pi(s), or directly to the machine-learning
 server(s).

## Contributing

Please adhere to [`contributing.md`](https://github.com/jeff1evesque/machine-learning/blob/master/contributing.md)
, when contributing code. Pull requests that deviate from the
 [`contributing.md`](https://github.com/jeff1evesque/machine-learning/blob/master/contributing.md)
, could be [labelled](https://github.com/jeff1evesque/machine-learning/labels)
 as `invalid`, and closed (without merging to master). These best practices
 will ensure integrity, when revisions of code, or issues need to be reviewed.

## Preconfiguration

This project implements puppet's [r10k](https://github.com/puppetlabs/r10k)
 module via vagrant's [plugin](https://github.com/jantman/vagrant-r10k). A
 requirement of this implementation includes a `Puppetfile` (already defined),
 which includes the following syntax:

```ruby
#!/usr/bin/env ruby
## Install Module: stdlib (apt dependency)
mod 'stdlib',
  :git => "git@github.com:puppetlabs/puppetlabs-stdlib.git",
  :ref => "4.6.0"

## Install Module: apt (from master)
mod 'apt',
  :git => "git@github.com:puppetlabs/puppetlabs-apt.git"
...
```

Specifically, this implements the ssh syntax `git@github.com:account/repo.git`,
 unlike the following alternatives:

- `https://github.com/account/repo.git`
- `git://github.com/account/repo.git`

This allows r10k to clone the corresponding puppet module(s), without a
 deterrence of [DDoS](https://en.wikipedia.org/wiki/Denial-of-service_attack).
 However, to implement the above syntax, ssh keys need to be generated, and
 properly assigned locally, as well as on the github account.

The following steps through how to implement the ssh keys with respect to
 github:

```bash
$ cd ~/.ssh/
$ ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
Enter file in which to save the key (/Users/you/.ssh/id_rsa): [Press enter]
Enter passphrase (empty for no passphrase): [Type a passphrase]
Enter same passphrase again: [Type passphrase again]
$ ssh-agent -s
Agent pid 59566
$ ssh-add ~/.ssh/id_rsa
$ pbcopy < ~/.ssh/id_rsa.pub
```

**Note:** it is recommended to simply press enter, to keep default values
 when asked *Enter file in which to save the key*.  Also, if `ssh-agent -s`
 alternative for git bash doesn't work, then `eval $(ssh-agent -s)` for other
 terminal prompts should work.

Then, at the top of any github page (after login), click `Settings > SSH keys >
 Add SSH Keys`, then paste the above copied key into the `Key` field, and click
 *Add key*.  Finally, to test the ssh connection, enter the following within
 the same terminal window used for the above commands:

```bash
$ ssh -T git@github.com
The authenticity of host 'github.com (207.97.227.239)' can't be established.
RSA key fingerprint is 16:27:ac:a5:76:28:2d:36:63:1b:56:4d:eb:df:a6:48.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added 'github.com,192.30.252.130' (RSA) to the list of
known hosts.
Hi jeff1evesque! You've successfully authenticated, but GitHub does not provide
shell access.
```

## Configuration

Fork this project in your GitHub account.  Then, clone your repository, with
 one of the following approaches:

- [simple clone](https://github.com/jeff1evesque/machine-learning/blob/master/README.md#simple-clone):
 clone the remote master branch.
- [commit hash](https://github.com/jeff1evesque/machine-learning/blob/master/README.md#commit-hash):
 clone the remote master branch, then checkout a specific commit hash.
- [release tag](https://github.com/jeff1evesque/machine-learning/blob/master/README.md#release-tag):
 clone the remote branch, associated with the desired release tag.

### Simple clone

```bash
cd /[destination-directory]
sudo git clone https://[account]@github.com/[account]/machine-learning.git
cd machine-learning
git remote add upstream https://github.com/[account]/machine-learning.git
```

**Note:** `[destination-directory]` corresponds to the desired directory path,
 where the project repository resides.  `[account]` corresponds to the git
 username, where the repository is being cloned from.  If the original
 repository was forked, then use your git username, otherwise, use
 `jeff1evesque`.

### Commit hash

```bash
cd /[destination-directory]
sudo git clone https://[account]@github.com/[account]/machine-learning.git
cd machine-learning
git remote add upstream https://github.com/[account]/machine-learning.git
# stop vagrant
vagrant halt
# ensure diffs don't prevent checkout, then checkout hash
git checkout -- .
git checkout [hash]
```

**Note:** the hashes associated with a release, can be found under the
 corresponding tag value, on the [release](https://github.com/jeff1evesque/machine-learning/releases)
 page.

**Note:** `[destination-directory]` corresponds to the desired directory path,
 where the project repository resides.  `[account]` corresponds to the git
 username, where the repository is being cloned from.  If the original
 repository was forked, then use your git username, otherwise, use
 `jeff1evesque`.

### Release tag

```bash
cd /[destination-directory]
# clone release tag: master branch does not exist
sudo git clone -b [release-tag] --single-branch --depth 1 https://github.com/[account]/machine-learning.git [destination-directory]
git remote add upstream https://github.com/[account]/machine-learning.git
# create master branch from remote master
cd machine-learning
git checkout -b master
git pull upstream master
# return to release tag branch
git checkout [release-tag]
```

**Note:** `[release-tag]` corresponds to the [release tag](https://github.com/jeff1evesque/machine-learning/tags)
 value, used to distinguish between releases.

**Note:** `[destination-directory]` corresponds to the desired directory path,
 where the project repository resides.  `[account]` corresponds to the git
 username, where the repository is being cloned from.  If the original
 repository was forked, then use your git username, otherwise, use
 `jeff1evesque`.

## Installation

In order to proceed with the installation for this project, two dependencies
 need to be installed:

- [Vagrant](https://www.vagrantup.com/)
- [Virtualbox](https://www.virtualbox.org/) (with extension pack)

Once the necessary dependencies have been installed, execute the following
 command to build the virtual environment:

```bash
cd /path/to/machine-learning/
vagrant up
```

Depending on the network speed, the build can take between 10-15 minutes. So,
 grab a cup of coffee, and perhaps enjoy a danish while the virtual machine
 builds. Remember, the application is intended to run on localhost, where the
 [`Vagrantfile`](https://github.com/jeff1evesque/machine-learning/blob/master/Vagrantfile)
 defines the exact port-forward on the host machine.

**Note:** a more complete refresher on virtualization, can be found within the
 vagrant [wiki page](https://github.com/jeff1evesque/machine-learning/wiki/Vagrant).

The following lines, indicate the application is accessible via
 `localhost:8080`, on the host machine:

```bash
...
  ## Create a forwarded port mapping which allows access to a specific port
  #  within the machine from a port on the host machine. In the example below,
  #  accessing "localhost:8080" will access port 80 on the guest machine.
  config.vm.network "forwarded_port", guest: 5000, host: 8080
  config.vm.network "forwarded_port", guest: 443, host: 8585
...
```

Otherwise, if ssl is configured, then the application is accessible via
 `https://localhost:8585`, on the host machine.

**Note:** general convention implements port `443` for ssl.

## Testing / Execution

### Web Interface

The [web-interface](https://github.com/jeff1evesque/machine-learning/blob/master/interface/templates/index.html)
, or GUI implementation, allow users to implement the following sessions:

- `data_new`: store the provided dataset(s), within the implemented sql
 database.
- `data_append`: append additional dataset(s), to an existing representation
 (from an earlier `data_new` session), within the implemented sql database.
- `model_generate`: using previous stored dataset(s) (from an earlier
 `data_new`, or `data_append` session), generate a corresponding model into the
 implemented nosql datastore.
- `model_predict`: using a previous stored model (from an earlier
 `model_predict` session), from the implemented nosql datastore, along with
 user supplied values, generate a corresponding prediction.

When using the web-interface, it is important to ensure the csv, xml, or json
 file(s), representing the corresponding dataset(s), are properly formatted.
 Dataset(s) poorly formatted will fail to create respective json dataset
 representation(s). Subsequently, the dataset(s) will not succeed being stored
 into corresponding database tables; therefore, no model, or prediction can be
 made.

The following are acceptable syntax:

- [CSV sample datasets](https://github.com/jeff1evesque/machine-learning/tree/master/interface/static/data/csv/)
- [XML sample datasets](https://github.com/jeff1evesque/machine-learning/tree/master/interface/static/data/xml/)
- [JSON sample datasets](https://github.com/jeff1evesque/machine-learning/tree/master/interface/static/data/json/web_interface)

**Note:** each dependent variable value (for JSON datasets), is an array
 (square brackets), since each dependent variable may have multiple
 observations.

As mentioned earlier, the web application can be accessed after subsequent
 `vagrant up` command, followed by using a browser referencing localhost:8080
 (or [https://localhost:5050](https://localhost:5050), with ssl), on the host
 machine.

### Programmatic Interface

The programmatic-interface, or set of API, allow users to implement the
 following sessions:

- `data_new`: store the provided dataset(s), within the implemented sql
 database.
- `data_append`: append additional dataset(s), to an existing representation
 (from an earlier `data_new` session), within the implemented sql database.
- `model_generate`: using previous stored dataset(s) (from an earlier
 `data_new`, or `data_append` session), generate a corresponding model into
 the implemented nosql datastore.
- `model_predict`: using a previous stored model (from an earlier
 `model_predict` session), from the implemented nosql datastore, along with
 user supplied values, generate a corresponding prediction.

A post request, can be implemented in python, as follows:

```python
import requests

endpoint_url = 'http://localhost:8080/load-data/'
headers = {'Content-Type': 'application/json'}

requests.post(endpoint_url, headers=headers, data=json_string_here)
```

**Note:** the above `post` request, can be implemented in a different language,
 respectively.

Some additional sample files have been provided, which outline how the `data`
 attribute implement should be implemented, with respect to the above `post`
 implementation:

- [SVM sample datasets](https://github.com/jeff1evesque/machine-learning/blob/master/interface/static/data/json/programmatic_interface/svm)
- [SVR sample datasets](https://github.com/jeff1evesque/machine-learning/blob/master/interface/static/data/json/programmatic_interface/svr)

**Note:** the content of each of the above files, can substituted for the above
 `data` attribute.

#### Data Attributes

The following (non-exhaustive) properties define the above implemented `data`
 attribute:

- `model_id`: the numeric id value, of the generated model in the nosql
 datastore.
- `model_type`: corresponds to the desired model type, which can be one of
 the following:
  - `classification`
  - `regression`
- `session_id`: the numeric id value, that represents the dataset stored in
 the sql database.
- `session_type`: corresponds to one of the following session types:
  - `data_new`
  - `data_append`
  - `model_generate`
  - `model_predict`
- `svm_dataset_type`: corresponds to one of the following dataset types:
  - `json_string`: indicate that the dataset is being sent via a `post` request
- `sv_kernel_type`: the type of kernel to apply to the support vector
 `model_type`:
  - `linear`
  - `polynomial`
  - `rbf`
  - `sigmoid`

### Test Scripts

This project implements [unit testing](https://en.wikipedia.org/wiki/Unit_testing),
 to validate logic in a consistent fashion. Currently, only high-level unit
 tests have been defined within [`pytest_svm_session.py`](https://github.com/jeff1evesque/machine-learning/blob/master/test/programmatic_interface/pytest_svm_session.py),
 and [`pytest_svr_session.py`](https://github.com/jeff1evesque/machine-learning/blob/master/test/programmatic_interface/pytest_svr_session.py).
 These unit tests have been automated within corresponding travis [builds](https://travis-ci.org/jeff1evesque/machine-learning),
 using a series of docker containers, connected via a common docker network:

- [`.travis.yml`](https://github.com/jeff1evesque/machine-learning/blob/e83f4222a9de11fcd839d6b3e789d63bab82e093/.travis.yml#L101-L120)
- [`default.dockerfile`](https://github.com/jeff1evesque/machine-learning/blob/master/default.dockerfile)
- [`database.dockerfile`](https://github.com/jeff1evesque/machine-learning/blob/master/database.dockerfile)
- [`redis.dockerfile`](https://github.com/jeff1evesque/machine-learning/blob/master/redis.dockerfile)
- [`webserver.dockerfile`](https://github.com/jeff1evesque/machine-learning/blob/master/webserver.dockerfile)

Current unit tests cover the following sessions:

- `data_new`
- `data_append`
- `model_predict`
- `model_generate`

which can be executed manually as follows:

```bash
$ cd /path/to/machine-learning/
$ vagrant up
$ vagrant ssh
vagrant@vagrant-ubuntu-trusty-64:~$ cd /vagrant/test && py.test manual
============================================ test session starts =============================================
platform linux2 -- Python 2.7.6, pytest-2.9.2, py-1.4.31, pluggy-0.3.1
rootdir: /vagrant/test/manual, inifile: pytest.ini
plugins: flask-0.10.0
collected 8 items

manual/programmatic_interface/pytest_svm_session.py ....
manual/programmatic_interface/pytest_svr_session.py ....

========================================= 8 passed in 7.82 seconds ==========================================
```

**Note:** future releases (i.e. milestone [1.0](https://github.com/jeff1evesque/machine-learning/milestones/1.0)),
 will include more granular unit tests.

**Note:** every script within this repository, with the
 [exception](https://github.com/jeff1evesque/machine-learning/issues/2234#issuecomment-158850974)
 of puppet (erb) [templates](https://github.com/jeff1evesque/machine-learning/tree/master/puppet/template),
 and a handful of open source libraries, have been [linted](https://en.wikipedia.org/wiki/Lint_%28software%29)
 via [`.travis.yml`](https://github.com/jeff1evesque/machine-learning/blob/master/.travis.yml).