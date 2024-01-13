# Debugging GCP Logs

+++++++++++++++++

LOGS FROM A WORKING DEPLOYMENT START
2024-01-03T02:29:53.7614146Z Requested labels: ubuntu-latest
2024-01-03T02:29:53.7614470Z Job defined at: freemocap/skellybot/.github/workflows/google-cloudrun-docker.yml@refs/heads/main
2024-01-03T02:29:53.7614583Z Waiting for a runner to pick up this job...
2024-01-03T02:29:54.2561592Z Job is waiting for a hosted runner to come online.
2024-01-03T02:29:56.6453920Z Job is about to start running on the hosted runner: GitHub Actions 3 (hosted)
2024-01-03T02:29:59.5656315Z Current runner version: '2.311.0'
2024-01-03T02:29:59.5679991Z ##[group]Operating System
2024-01-03T02:29:59.5680625Z Ubuntu
2024-01-03T02:29:59.5680976Z 22.04.3
2024-01-03T02:29:59.5681406Z LTS
2024-01-03T02:29:59.5681748Z ##[endgroup]
2024-01-03T02:29:59.5682144Z ##[group]Runner Image
2024-01-03T02:29:59.5682613Z Image: ubuntu-22.04
2024-01-03T02:29:59.5683041Z Version: 20231217.2.0
2024-01-03T02:29:59.5684045Z Included Software: https://github.com/actions/runner-images/blob/ubuntu22/20231217.2/images/ubuntu/Ubuntu2204-Readme.md
2024-01-03T02:29:59.5685560Z Image Release: https://github.com/actions/runner-images/releases/tag/ubuntu22%2F20231217.2
2024-01-03T02:29:59.5686470Z ##[endgroup]
2024-01-03T02:29:59.5686929Z ##[group]Runner Image Provisioner
2024-01-03T02:29:59.5687377Z 2.0.321.1
2024-01-03T02:29:59.5687731Z ##[endgroup]
2024-01-03T02:29:59.5688636Z ##[group]GITHUB_TOKEN Permissions
2024-01-03T02:29:59.5690238Z Contents: read
2024-01-03T02:29:59.5690645Z Metadata: read
2024-01-03T02:29:59.5691568Z ##[endgroup]
2024-01-03T02:29:59.5695173Z Secret source: Actions
2024-01-03T02:29:59.5695768Z Prepare workflow directory
2024-01-03T02:29:59.6441894Z Prepare all required actions
2024-01-03T02:29:59.6599229Z Getting action download info
2024-01-03T02:29:59.8945647Z Download action repository 'actions/checkout@v4' (SHA:b4ffde65f46336ab88eb53be808477a3936bae11)
2024-01-03T02:29:59.9994072Z Download action repository 'google-github-actions/auth@v2' (SHA:67e9c72af6e0492df856527b474995862b7b6591)
2024-01-03T02:30:00.3809052Z Download action repository 'docker/login-action@v3' (SHA:343f7c4344506bcbf9b4de18042ae17996df046d)
2024-01-03T02:30:00.8510897Z Complete job name: deploy
2024-01-03T02:30:00.9447399Z ##[group]Run actions/checkout@v4
2024-01-03T02:30:00.9447994Z with:
2024-01-03T02:30:00.9448431Z   repository: freemocap/skellybot
2024-01-03T02:30:00.9449317Z   token: ***
2024-01-03T02:30:00.9449741Z   ssh-strict: true
2024-01-03T02:30:00.9450280Z   persist-credentials: true
2024-01-03T02:30:00.9450779Z   clean: true
2024-01-03T02:30:00.9451196Z   sparse-checkout-cone-mode: true
2024-01-03T02:30:00.9451825Z   fetch-depth: 1
2024-01-03T02:30:00.9452237Z   fetch-tags: false
2024-01-03T02:30:00.9452689Z   show-progress: true
2024-01-03T02:30:00.9453198Z   lfs: false
2024-01-03T02:30:00.9453580Z   submodules: false
2024-01-03T02:30:00.9454011Z   set-safe-directory: true
2024-01-03T02:30:00.9454762Z env:
2024-01-03T02:30:00.9455177Z   PROJECT_ID: mocap-test-project
2024-01-03T02:30:00.9455741Z   GAR_LOCATION: us-east1
2024-01-03T02:30:00.9456280Z   SERVICE: jonbot/nestbot
2024-01-03T02:30:00.9456727Z   REGION: us-central1
2024-01-03T02:30:00.9457153Z ##[endgroup]
2024-01-03T02:30:01.1123271Z Syncing repository: freemocap/skellybot
2024-01-03T02:30:01.1126047Z ##[group]Getting Git version info
2024-01-03T02:30:01.1127407Z Working directory is '/home/runner/work/skellybot/skellybot'
2024-01-03T02:30:01.1129229Z [command]/usr/bin/git version
2024-01-03T02:30:01.1130071Z git version 2.43.0
2024-01-03T02:30:01.1138783Z ##[endgroup]
2024-01-03T02:30:01.1156178Z Temporarily overriding HOME='/home/runner/work/_temp/8e322c3b-8ac5-4670-91c4-8931b19ebe76' before making global git config changes
2024-01-03T02:30:01.1158675Z Adding repository directory to the temporary git global config as a safe directory
2024-01-03T02:30:01.1161040Z [command]/usr/bin/git config --global --add safe.directory /home/runner/work/skellybot/skellybot
2024-01-03T02:30:01.1193313Z Deleting the contents of '/home/runner/work/skellybot/skellybot'
2024-01-03T02:30:01.1198826Z ##[group]Initializing the repository
2024-01-03T02:30:01.1201721Z [command]/usr/bin/git init /home/runner/work/skellybot/skellybot
2024-01-03T02:30:01.1292342Z hint: Using 'master' as the name for the initial branch. This default branch name
2024-01-03T02:30:01.1294208Z hint: is subject to change. To configure the initial branch name to use in all
2024-01-03T02:30:01.1295559Z hint: of your new repositories, which will suppress this warning, call:
2024-01-03T02:30:01.1296498Z hint: 
2024-01-03T02:30:01.1297388Z hint: 	git config --global init.defaultBranch <name>
2024-01-03T02:30:01.1298143Z hint: 
2024-01-03T02:30:01.1298945Z hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
2024-01-03T02:30:01.1300099Z hint: 'development'. The just-created branch can be renamed via this command:
2024-01-03T02:30:01.1301021Z hint: 
2024-01-03T02:30:01.1301474Z hint: 	git branch -m <name>
2024-01-03T02:30:01.1308816Z Initialized empty Git repository in /home/runner/work/skellybot/skellybot/.git/
2024-01-03T02:30:01.1317469Z [command]/usr/bin/git remote add origin https://github.com/freemocap/skellybot
2024-01-03T02:30:01.1354496Z ##[endgroup]
2024-01-03T02:30:01.1355344Z ##[group]Disabling automatic garbage collection
2024-01-03T02:30:01.1356756Z [command]/usr/bin/git config --local gc.auto 0
2024-01-03T02:30:01.1385198Z ##[endgroup]
2024-01-03T02:30:01.1385958Z ##[group]Setting up auth
2024-01-03T02:30:01.1389979Z [command]/usr/bin/git config --local --name-only --get-regexp core\.sshCommand
2024-01-03T02:30:01.1418497Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"
2024-01-03T02:30:01.1760124Z [command]/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
2024-01-03T02:30:01.1787919Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :"
2024-01-03T02:30:01.2018640Z [command]/usr/bin/git config --local http.https://github.com/.extraheader AUTHORIZATION: basic ***
2024-01-03T02:30:01.2051175Z ##[endgroup]
2024-01-03T02:30:01.2052201Z ##[group]Fetching the repository
2024-01-03T02:30:01.2064032Z [command]/usr/bin/git -c protocol.version=2 fetch --no-tags --prune --no-recurse-submodules --depth=1 origin +676f2b55cf418a17d13170730d6e74fdec198dea:refs/remotes/origin/main
2024-01-03T02:30:01.7113362Z From https://github.com/freemocap/skellybot
2024-01-03T02:30:01.7114390Z  * [new ref]         676f2b55cf418a17d13170730d6e74fdec198dea -> origin/main
2024-01-03T02:30:01.7142315Z ##[endgroup]
2024-01-03T02:30:01.7143428Z ##[group]Determining the checkout info
2024-01-03T02:30:01.7144804Z ##[endgroup]
2024-01-03T02:30:01.7145806Z ##[group]Checking out the ref
2024-01-03T02:30:01.7150092Z [command]/usr/bin/git checkout --progress --force -B main refs/remotes/origin/main
2024-01-03T02:30:01.7893649Z Switched to a new branch 'main'
2024-01-03T02:30:01.7895770Z branch 'main' set up to track 'origin/main'.
2024-01-03T02:30:01.7905912Z ##[endgroup]
2024-01-03T02:30:01.7944731Z [command]/usr/bin/git log -1 --format='%H'
2024-01-03T02:30:01.7968849Z '676f2b55cf418a17d13170730d6e74fdec198dea'
2024-01-03T02:30:01.8296540Z ##[group]Run google-github-actions/auth@v2
2024-01-03T02:30:01.8297068Z with:
2024-01-03T02:30:01.8297440Z   project_id: mocap-test-project
2024-01-03T02:30:01.8297975Z   token_format: access_token
2024-01-03T02:30:01.8299159Z   workload_identity_provider: ***
2024-01-03T02:30:01.8299977Z   service_account: ***
2024-01-03T02:30:01.8300373Z   create_credentials_file: true
2024-01-03T02:30:01.8300924Z   export_environment_variables: true
2024-01-03T02:30:01.8301355Z   universe: googleapis.com
2024-01-03T02:30:01.8301720Z   cleanup_credentials: true
2024-01-03T02:30:01.8302114Z   access_token_lifetime: 3600s
2024-01-03T02:30:01.8302654Z   access_token_scopes: https://www.googleapis.com/auth/cloud-platform
2024-01-03T02:30:01.8303271Z   retries: 3
2024-01-03T02:30:01.8303589Z   backoff: 250
2024-01-03T02:30:01.8303949Z   id_token_include_email: false
2024-01-03T02:30:01.8304370Z env:
2024-01-03T02:30:01.8304694Z   PROJECT_ID: mocap-test-project
2024-01-03T02:30:01.8305289Z   GAR_LOCATION: us-east1
2024-01-03T02:30:01.8305662Z   SERVICE: jonbot/nestbot
2024-01-03T02:30:01.8306011Z   REGION: us-central1
2024-01-03T02:30:01.8306409Z ##[endgroup]
2024-01-03T02:30:02.0683904Z Created credentials file at "/home/runner/work/skellybot/skellybot/gha-creds-4199cb2c73bcb4f5.json"
2024-01-03T02:30:02.3122620Z ##[group]Run docker/login-action@v3
2024-01-03T02:30:02.3123133Z with:
2024-01-03T02:30:02.3123565Z   username: oauth2accesstoken
2024-01-03T02:30:02.3129361Z   password: ***
2024-01-03T02:30:02.3129757Z   registry: us-east1-docker.pkg.dev
2024-01-03T02:30:02.3130248Z   ecr: auto
2024-01-03T02:30:02.3130593Z   logout: true
2024-01-03T02:30:02.3130985Z env:
2024-01-03T02:30:02.3131336Z   PROJECT_ID: mocap-test-project
2024-01-03T02:30:02.3131967Z   GAR_LOCATION: us-east1
2024-01-03T02:30:02.3132515Z   SERVICE: jonbot/nestbot
2024-01-03T02:30:02.3132917Z   REGION: us-central1
2024-01-03T02:30:02.3133615Z   CLOUDSDK_AUTH_CREDENTIAL_FILE_OVERRIDE: /home/runner/work/skellybot/skellybot/gha-creds-4199cb2c73bcb4f5.json
2024-01-03T02:30:02.3135282Z   GOOGLE_APPLICATION_CREDENTIALS: /home/runner/work/skellybot/skellybot/gha-creds-4199cb2c73bcb4f5.json
2024-01-03T02:30:02.3136408Z   GOOGLE_GHA_CREDS_PATH: /home/runner/work/skellybot/skellybot/gha-creds-4199cb2c73bcb4f5.json
2024-01-03T02:30:02.3137352Z   CLOUDSDK_CORE_PROJECT: mocap-test-project
2024-01-03T02:30:02.3137844Z   CLOUDSDK_PROJECT: mocap-test-project
2024-01-03T02:30:02.3138352Z   GCLOUD_PROJECT: mocap-test-project
2024-01-03T02:30:02.3138811Z   GCP_PROJECT: mocap-test-project
2024-01-03T02:30:02.3139254Z   GOOGLE_CLOUD_PROJECT: mocap-test-project
2024-01-03T02:30:02.3139770Z ##[endgroup]
2024-01-03T02:30:02.4143911Z Logging into us-east1-docker.pkg.dev...
2024-01-03T02:30:03.1215891Z Login Succeeded!
2024-01-03T02:30:03.1328630Z ##[group]Run docker build -t "us-east1-docker.pkg.dev/mocap-test-project/jonbot/nestbot:676f2b55cf418a17d13170730d6e74fdec198dea" ./
2024-01-03T02:30:03.1330041Z [36;1mdocker build -t "us-east1-docker.pkg.dev/mocap-test-project/jonbot/nestbot:676f2b55cf418a17d13170730d6e74fdec198dea" ./[0m
2024-01-03T02:30:03.1331288Z [36;1mdocker build -t "us-east1-docker.pkg.dev/mocap-test-project/jonbot/nestbot:latest" ./[0m
2024-01-03T02:30:03.1332362Z [36;1mdocker push "us-east1-docker.pkg.dev/mocap-test-project/jonbot/nestbot:676f2b55cf418a17d13170730d6e74fdec198dea"[0m
2024-01-03T02:30:03.1333390Z [36;1mdocker push "us-east1-docker.pkg.dev/mocap-test-project/jonbot/nestbot:latest"[0m
2024-01-03T02:30:03.1398166Z shell: /usr/bin/bash -e {0}
2024-01-03T02:30:03.1398614Z env:
2024-01-03T02:30:03.1398957Z   PROJECT_ID: mocap-test-project
2024-01-03T02:30:03.1399454Z   GAR_LOCATION: us-east1
2024-01-03T02:30:03.1399899Z   SERVICE: jonbot/nestbot
2024-01-03T02:30:03.1400383Z   REGION: us-central1
2024-01-03T02:30:03.1401134Z   CLOUDSDK_AUTH_CREDENTIAL_FILE_OVERRIDE: /home/runner/work/skellybot/skellybot/gha-creds-4199cb2c73bcb4f5.json
2024-01-03T02:30:03.1402157Z   GOOGLE_APPLICATION_CREDENTIALS: /home/runner/work/skellybot/skellybot/gha-creds-4199cb2c73bcb4f5.json
2024-01-03T02:30:03.1403170Z   GOOGLE_GHA_CREDS_PATH: /home/runner/work/skellybot/skellybot/gha-creds-4199cb2c73bcb4f5.json
2024-01-03T02:30:03.1403861Z   CLOUDSDK_CORE_PROJECT: mocap-test-project
2024-01-03T02:30:03.1404425Z   CLOUDSDK_PROJECT: mocap-test-project
2024-01-03T02:30:03.1404914Z   GCLOUD_PROJECT: mocap-test-project
2024-01-03T02:30:03.1405342Z   GCP_PROJECT: mocap-test-project
2024-01-03T02:30:03.1405869Z   GOOGLE_CLOUD_PROJECT: mocap-test-project
2024-01-03T02:30:03.1406307Z ##[endgroup]
2024-01-03T02:30:03.5675877Z #0 building with "default" instance using docker driver
2024-01-03T02:30:03.5677115Z 
2024-01-03T02:30:03.5680802Z #1 [internal] load build definition from Dockerfile
2024-01-03T02:30:03.5681712Z #1 transferring dockerfile: 1.03kB done
2024-01-03T02:30:03.5682574Z #1 DONE 0.0s
2024-01-03T02:30:03.5682807Z 
2024-01-03T02:30:03.5683055Z #2 [internal] load .dockerignore
2024-01-03T02:30:03.5684375Z #2 transferring context: 57B done
2024-01-03T02:30:03.5685131Z #2 DONE 0.0s
2024-01-03T02:30:03.5685465Z 
2024-01-03T02:30:03.5686139Z #3 [auth] docker/dockerfile:pull token for registry-1.docker.io
2024-01-03T02:30:03.5687136Z #3 DONE 0.0s
2024-01-03T02:30:03.5687807Z 
2024-01-03T02:30:03.5688186Z #4 resolve image config for docker.io/docker/dockerfile:1.2
2024-01-03T02:30:04.7706417Z #4 DONE 1.3s
2024-01-03T02:30:04.7706835Z 
2024-01-03T02:30:04.7707888Z #5 docker-image://docker.io/docker/dockerfile:1.2@sha256:e2a8561e419ab1ba6b2fe6cbdf49fd92b95912df1cf7d313c3e2230a333fdbcc
2024-01-03T02:30:04.7709381Z #5 resolve docker.io/docker/dockerfile:1.2@sha256:e2a8561e419ab1ba6b2fe6cbdf49fd92b95912df1cf7d313c3e2230a333fdbcc done
2024-01-03T02:30:04.8953859Z #5 sha256:86e43bba076d67c1a890cbc07813806b11eca53843dc643202d939b986c8c332 1.21kB / 1.21kB done
2024-01-03T02:30:04.8955766Z #5 sha256:3cc8e449ce9f6e0752ede8f50a7334bf0c7b2d24d76da2ffae7aa6a729dd1da4 9.64MB / 9.64MB 0.2s done
2024-01-03T02:30:04.8957452Z #5 sha256:e2a8561e419ab1ba6b2fe6cbdf49fd92b95912df1cf7d313c3e2230a333fdbcc 1.69kB / 1.69kB done
2024-01-03T02:30:04.8959009Z #5 sha256:e3ee2e6b536452d876b1c5aa12db9bca51b8f52b2505178cae6d13e33daeed2b 528B / 528B done
2024-01-03T02:30:04.8960581Z #5 extracting sha256:3cc8e449ce9f6e0752ede8f50a7334bf0c7b2d24d76da2ffae7aa6a729dd1da4
2024-01-03T02:30:05.0450864Z #5 extracting sha256:3cc8e449ce9f6e0752ede8f50a7334bf0c7b2d24d76da2ffae7aa6a729dd1da4 0.1s done
2024-01-03T02:30:05.0451847Z #5 DONE 0.3s
2024-01-03T02:30:05.1957540Z 
2024-01-03T02:30:05.1959197Z #6 [internal] load .dockerignore
2024-01-03T02:30:05.1960100Z #6 DONE 0.0s
2024-01-03T02:30:05.1960377Z 
2024-01-03T02:30:05.1960659Z #7 [internal] load build definition from Dockerfile
2024-01-03T02:30:05.1961364Z #7 DONE 0.0s
2024-01-03T02:30:05.1961621Z 
2024-01-03T02:30:05.1962522Z #8 [auth] library/node:pull token for registry-1.docker.io
2024-01-03T02:30:05.1963205Z #8 DONE 0.0s
2024-01-03T02:30:05.1963560Z 
2024-01-03T02:30:05.1963987Z #9 [internal] load metadata for docker.io/library/node:20.10.0-slim
2024-01-03T02:30:05.4801757Z #9 DONE 0.4s
2024-01-03T02:30:05.6301975Z 
2024-01-03T02:30:05.6304741Z #10 [stage-0  1/12] FROM docker.io/library/node:20.10.0-slim@sha256:5c714c3e90f66a2cbfa266b90a4d7adcd63453cd730aa2d13cba84b260bea2e6
2024-01-03T02:30:05.6307537Z #10 resolve docker.io/library/node:20.10.0-slim@sha256:5c714c3e90f66a2cbfa266b90a4d7adcd63453cd730aa2d13cba84b260bea2e6 done
2024-01-03T02:30:05.7402719Z #10 ...
2024-01-03T02:30:05.7403008Z 
2024-01-03T02:30:05.7403249Z #11 [internal] load build context
2024-01-03T02:30:05.7404120Z #11 transferring context: 20.31MB 0.2s done
2024-01-03T02:30:05.7404618Z #11 DONE 0.2s
2024-01-03T02:30:05.7404800Z 
2024-01-03T02:30:05.7405790Z #10 [stage-0  1/12] FROM docker.io/library/node:20.10.0-slim@sha256:5c714c3e90f66a2cbfa266b90a4d7adcd63453cd730aa2d13cba84b260bea2e6
2024-01-03T02:30:05.7406930Z #10 sha256:5c714c3e90f66a2cbfa266b90a4d7adcd63453cd730aa2d13cba84b260bea2e6 1.21kB / 1.21kB done
2024-01-03T02:30:05.7407874Z #10 sha256:df49e2dc50b7b1f91b44201432cefaf034f66e549bcbd3a29745ffff439afc9e 1.37kB / 1.37kB done
2024-01-03T02:30:05.7408881Z #10 sha256:03f4750834334638efe8f99b5b6c69c08048988fe711078c6889d536dc88aea1 7.62kB / 7.62kB done
2024-01-03T02:30:05.7409821Z #10 sha256:af107e978371b6cd6339127a05502c5eacd1e6b0e9eb7b2f4aa7b6fc87e2dd81 14.68MB / 29.13MB 0.2s
2024-01-03T02:30:05.7410758Z #10 sha256:ebd7ac832a7e4bd07f5ad6f4bbc6db1f5b02de7a8e07b40627142ef61a9b1b9d 0B / 3.36kB 0.2s
2024-01-03T02:30:05.7411769Z #10 sha256:c5da3822f0fa5def8cc49ddb050ab51e134b313fe72ac31489d0303587f27281 3.15MB / 40.46MB 0.2s
2024-01-03T02:30:05.8436453Z #10 sha256:af107e978371b6cd6339127a05502c5eacd1e6b0e9eb7b2f4aa7b6fc87e2dd81 28.31MB / 29.13MB 0.3s
2024-01-03T02:30:05.8438267Z #10 sha256:ebd7ac832a7e4bd07f5ad6f4bbc6db1f5b02de7a8e07b40627142ef61a9b1b9d 3.36kB / 3.36kB 0.2s done
2024-01-03T02:30:05.8440073Z #10 sha256:c5da3822f0fa5def8cc49ddb050ab51e134b313fe72ac31489d0303587f27281 14.68MB / 40.46MB 0.3s
2024-01-03T02:30:05.8441826Z #10 sha256:e21beee6f6d33b4605828c995958d12a7fb3762621c15d3c4355bfed122a11f0 0B / 2.67MB 0.3s
2024-01-03T02:30:05.9942847Z #10 sha256:af107e978371b6cd6339127a05502c5eacd1e6b0e9eb7b2f4aa7b6fc87e2dd81 29.13MB / 29.13MB 0.3s done
2024-01-03T02:30:05.9946843Z #10 sha256:c5da3822f0fa5def8cc49ddb050ab51e134b313fe72ac31489d0303587f27281 29.36MB / 40.46MB 0.4s
2024-01-03T02:30:05.9948296Z #10 sha256:e21beee6f6d33b4605828c995958d12a7fb3762621c15d3c4355bfed122a11f0 2.67MB / 2.67MB 0.3s done
2024-01-03T02:30:05.9950738Z #10 extracting sha256:af107e978371b6cd6339127a05502c5eacd1e6b0e9eb7b2f4aa7b6fc87e2dd81
2024-01-03T02:30:05.9952239Z #10 sha256:6e2165efc3a7fb15942e607201f825c49ec4b664e3988e01e2e4a78b682da50e 451B / 451B 0.4s done
2024-01-03T02:30:06.1280381Z #10 sha256:c5da3822f0fa5def8cc49ddb050ab51e134b313fe72ac31489d0303587f27281 32.51MB / 40.46MB 0.5s
2024-01-03T02:30:06.2310865Z #10 sha256:c5da3822f0fa5def8cc49ddb050ab51e134b313fe72ac31489d0303587f27281 39.85MB / 40.46MB 0.6s
2024-01-03T02:30:06.4834103Z #10 sha256:c5da3822f0fa5def8cc49ddb050ab51e134b313fe72ac31489d0303587f27281 40.46MB / 40.46MB 0.8s done
2024-01-03T02:30:07.0468504Z #10 extracting sha256:af107e978371b6cd6339127a05502c5eacd1e6b0e9eb7b2f4aa7b6fc87e2dd81 1.1s done
2024-01-03T02:30:07.0470374Z #10 extracting sha256:ebd7ac832a7e4bd07f5ad6f4bbc6db1f5b02de7a8e07b40627142ef61a9b1b9d done
2024-01-03T02:30:07.0472008Z #10 extracting sha256:c5da3822f0fa5def8cc49ddb050ab51e134b313fe72ac31489d0303587f27281
2024-01-03T02:30:08.3706187Z #10 extracting sha256:c5da3822f0fa5def8cc49ddb050ab51e134b313fe72ac31489d0303587f27281 1.2s done
2024-01-03T02:30:08.4996516Z #10 extracting sha256:e21beee6f6d33b4605828c995958d12a7fb3762621c15d3c4355bfed122a11f0 0.1s done
2024-01-03T02:30:08.6500595Z #10 extracting sha256:6e2165efc3a7fb15942e607201f825c49ec4b664e3988e01e2e4a78b682da50e done
2024-01-03T02:30:08.6501707Z #10 DONE 3.0s
2024-01-03T02:30:08.6501958Z 
2024-01-03T02:30:08.6502464Z #12 [stage-0  2/12] WORKDIR /workspace
2024-01-03T02:30:08.6502928Z #12 DONE 0.0s
2024-01-03T02:30:08.6503157Z 
2024-01-03T02:30:08.6503463Z #13 [stage-0  3/12] RUN rm -rf /etc/apt/apt.conf.d/docker-clean
2024-01-03T02:30:08.7723124Z #13 DONE 0.2s
2024-01-03T02:30:08.9230362Z 
2024-01-03T02:30:08.9231550Z #14 [stage-0  4/12] COPY ./bin/builds/ .
2024-01-03T02:30:08.9232476Z #14 DONE 0.0s
2024-01-03T02:30:08.9232796Z 
2024-01-03T02:30:08.9233196Z #15 [stage-0  5/12] RUN mkdir /home/.npm
2024-01-03T02:30:09.0755519Z #15 DONE 0.2s
2024-01-03T02:30:09.0755920Z 
2024-01-03T02:30:09.0757098Z #16 [stage-0  6/12] RUN useradd -m appuser && chown -R appuser /workspace && chown -R appuser "/home/.npm"
2024-01-03T02:30:09.3744536Z #16 DONE 0.2s
2024-01-03T02:30:09.3744988Z 
2024-01-03T02:30:09.3747152Z #17 [stage-0  7/12] RUN --mount=type=cache,target=/var/cache/apt ./install_packages     dumb-init     htop     make     g++     python3
2024-01-03T02:30:11.0133189Z #17 1.689 Reading package lists...
2024-01-03T02:30:11.0134028Z #17 1.699 Building dependency tree...
2024-01-03T02:30:11.1636164Z #17 1.778 Reading state information...
2024-01-03T02:30:11.1637176Z #17 1.873 The following additional packages will be installed:
2024-01-03T02:30:11.1638927Z #17 1.873   binutils binutils-common binutils-x86-64-linux-gnu cpp cpp-12 g++-12 gcc
2024-01-03T02:30:11.1640512Z #17 1.873   gcc-12 libasan8 libatomic1 libbinutils libc-dev-bin libc6-dev libcc1-0
2024-01-03T02:30:11.1641952Z #17 1.873   libcrypt-dev libctf-nobfd0 libctf0 libexpat1 libgcc-12-dev libgomp1
2024-01-03T02:30:11.1643196Z #17 1.873   libgprofng0 libgssapi-krb5-2 libisl23 libitm1 libjansson4 libk5crypto3
2024-01-03T02:30:11.1644382Z #17 1.873   libkeyutils1 libkrb5-3 libkrb5support0 liblsan0 libmpc3 libmpfr6
2024-01-03T02:30:11.1645737Z #17 1.873   libncursesw6 libnl-3-200 libnl-genl-3-200 libnsl-dev libnsl2
2024-01-03T02:30:11.1647267Z #17 1.873   libpython3-stdlib libpython3.11-minimal libpython3.11-stdlib libquadmath0
2024-01-03T02:30:11.1648652Z #17 1.873   libreadline8 libsqlite3-0 libssl3 libstdc++-12-dev libtirpc-common
2024-01-03T02:30:11.1649727Z #17 1.874   libtirpc-dev libtirpc3 libtsan2 libubsan1 linux-libc-dev media-types
2024-01-03T02:30:11.1651310Z #17 1.874   python3-minimal python3.11 python3.11-minimal readline-common rpcsvc-proto
2024-01-03T02:30:11.1652404Z #17 1.874 Suggested packages:
2024-01-03T02:30:11.1654566Z #17 1.874   binutils-doc cpp-doc gcc-12-locales cpp-12-doc g++-multilib g++-12-multilib
2024-01-03T02:30:11.1656134Z #17 1.874   gcc-12-doc gcc-multilib manpages-dev autoconf automake libtool flex bison
2024-01-03T02:30:11.1657735Z #17 1.874   gdb gcc-doc gcc-12-multilib lm-sensors lsof strace glibc-doc krb5-doc
2024-01-03T02:30:11.1659219Z #17 1.874   krb5-user libstdc++-12-doc make-doc python3-doc python3-tk python3-venv
2024-01-03T02:30:11.1660276Z #17 1.874   python3.11-venv python3.11-doc binfmt-support readline-doc
2024-01-03T02:30:11.1661363Z #17 1.874 Recommended packages:
2024-01-03T02:30:11.1662512Z #17 1.874   manpages manpages-dev libc-devtools krb5-locales libgpm2 ca-certificates
2024-01-03T02:30:11.4648652Z #17 2.133 The following NEW packages will be installed:
2024-01-03T02:30:11.4650122Z #17 2.133   binutils binutils-common binutils-x86-64-linux-gnu cpp cpp-12 dumb-init g++
2024-01-03T02:30:11.4651261Z #17 2.133   g++-12 gcc gcc-12 htop libasan8 libatomic1 libbinutils libc-dev-bin
2024-01-03T02:30:11.4652223Z #17 2.133   libc6-dev libcc1-0 libcrypt-dev libctf-nobfd0 libctf0 libexpat1
2024-01-03T02:30:11.4653118Z #17 2.133   libgcc-12-dev libgomp1 libgprofng0 libgssapi-krb5-2 libisl23 libitm1
2024-01-03T02:30:11.4654099Z #17 2.133   libjansson4 libk5crypto3 libkeyutils1 libkrb5-3 libkrb5support0 liblsan0
2024-01-03T02:30:11.4655266Z #17 2.133   libmpc3 libmpfr6 libncursesw6 libnl-3-200 libnl-genl-3-200 libnsl-dev
2024-01-03T02:30:11.4656231Z #17 2.133   libnsl2 libpython3-stdlib libpython3.11-minimal libpython3.11-stdlib
2024-01-03T02:30:11.4657365Z #17 2.133   libquadmath0 libreadline8 libsqlite3-0 libssl3 libstdc++-12-dev
2024-01-03T02:30:11.4658328Z #17 2.133   libtirpc-common libtirpc-dev libtirpc3 libtsan2 libubsan1 linux-libc-dev
2024-01-03T02:30:11.4659371Z #17 2.134   make media-types python3 python3-minimal python3.11 python3.11-minimal
2024-01-03T02:30:11.4660095Z #17 2.134   readline-common rpcsvc-proto
2024-01-03T02:30:11.4660768Z #17 2.173 0 upgraded, 62 newly installed, 0 to remove and 0 not upgraded.
2024-01-03T02:30:11.4661412Z #17 2.173 Need to get 73.0 MB of archives.
2024-01-03T02:30:11.4662016Z #17 2.173 After this operation, 294 MB of additional disk space will be used.
2024-01-03T02:30:11.4663035Z #17 2.173 Get:1 http://deb.debian.org/debian bookworm/main amd64 libssl3 amd64 3.0.11-1~deb12u2 [2019 kB]
2024-01-03T02:30:11.5657225Z #17 2.256 Get:2 http://deb.debian.org/debian bookworm/main amd64 libpython3.11-minimal amd64 3.11.2-6 [813 kB]
2024-01-03T02:30:11.5659369Z #17 2.260 Get:3 http://deb.debian.org/debian bookworm/main amd64 libexpat1 amd64 2.5.0-1 [99.3 kB]
2024-01-03T02:30:11.5661218Z #17 2.263 Get:4 http://deb.debian.org/debian bookworm/main amd64 python3.11-minimal amd64 3.11.2-6 [2064 kB]
2024-01-03T02:30:11.5663189Z #17 2.273 Get:5 http://deb.debian.org/debian bookworm/main amd64 python3-minimal amd64 3.11.2-1+b1 [26.3 kB]
2024-01-03T02:30:11.5664995Z #17 2.273 Get:6 http://deb.debian.org/debian bookworm/main amd64 media-types all 10.0.0 [26.1 kB]
2024-01-03T02:30:11.5666497Z #17 2.273 Get:7 http://deb.debian.org/debian bookworm/main amd64 libncursesw6 amd64 6.4-4 [134 kB]
2024-01-03T02:30:11.5668170Z #17 2.274 Get:8 http://deb.debian.org/debian bookworm/main amd64 libkrb5support0 amd64 1.20.1-2+deb12u1 [32.4 kB]
2024-01-03T02:30:11.5670013Z #17 2.274 Get:9 http://deb.debian.org/debian bookworm/main amd64 libk5crypto3 amd64 1.20.1-2+deb12u1 [78.9 kB]
2024-01-03T02:30:11.5671198Z #17 2.275 Get:10 http://deb.debian.org/debian bookworm/main amd64 libkeyutils1 amd64 1.6.3-2 [8808 B]
2024-01-03T02:30:11.5672973Z #17 2.275 Get:11 http://deb.debian.org/debian bookworm/main amd64 libkrb5-3 amd64 1.20.1-2+deb12u1 [332 kB]
2024-01-03T02:30:11.5674978Z #17 2.280 Get:12 http://deb.debian.org/debian bookworm/main amd64 libgssapi-krb5-2 amd64 1.20.1-2+deb12u1 [134 kB]
2024-01-03T02:30:11.5676845Z #17 2.281 Get:13 http://deb.debian.org/debian bookworm/main amd64 libtirpc-common all 1.3.3+ds-1 [14.0 kB]
2024-01-03T02:30:11.5678819Z #17 2.292 Get:14 http://deb.debian.org/debian bookworm/main amd64 libtirpc3 amd64 1.3.3+ds-1 [85.2 kB]
2024-01-03T02:30:11.5680811Z #17 2.293 Get:15 http://deb.debian.org/debian bookworm/main amd64 libnsl2 amd64 1.3.0-2 [39.5 kB]
2024-01-03T02:30:11.5682690Z #17 2.294 Get:16 http://deb.debian.org/debian bookworm/main amd64 readline-common all 8.2-1.3 [69.0 kB]
2024-01-03T02:30:11.5684511Z #17 2.295 Get:17 http://deb.debian.org/debian bookworm/main amd64 libreadline8 amd64 8.2-1.3 [166 kB]
2024-01-03T02:30:11.5686252Z #17 2.296 Get:18 http://deb.debian.org/debian bookworm/main amd64 libsqlite3-0 amd64 3.40.1-2 [837 kB]
2024-01-03T02:30:11.5688258Z #17 2.300 Get:19 http://deb.debian.org/debian bookworm/main amd64 libpython3.11-stdlib amd64 3.11.2-6 [1796 kB]
2024-01-03T02:30:11.5690100Z #17 2.307 Get:20 http://deb.debian.org/debian bookworm/main amd64 python3.11 amd64 3.11.2-6 [572 kB]
2024-01-03T02:30:11.5691918Z #17 2.310 Get:21 http://deb.debian.org/debian bookworm/main amd64 libpython3-stdlib amd64 3.11.2-1+b1 [9312 B]
2024-01-03T02:30:11.5693912Z #17 2.310 Get:22 http://deb.debian.org/debian bookworm/main amd64 python3 amd64 3.11.2-1+b1 [26.3 kB]
2024-01-03T02:30:11.5696035Z #17 2.310 Get:23 http://deb.debian.org/debian bookworm/main amd64 binutils-common amd64 2.40-2 [2487 kB]
2024-01-03T02:30:11.5697911Z #17 2.321 Get:24 http://deb.debian.org/debian bookworm/main amd64 libbinutils amd64 2.40-2 [572 kB]
2024-01-03T02:30:11.5699713Z #17 2.323 Get:25 http://deb.debian.org/debian bookworm/main amd64 libctf-nobfd0 amd64 2.40-2 [153 kB]
2024-01-03T02:30:11.5701652Z #17 2.324 Get:26 http://deb.debian.org/debian bookworm/main amd64 libctf0 amd64 2.40-2 [89.8 kB]
2024-01-03T02:30:11.5703481Z #17 2.325 Get:27 http://deb.debian.org/debian bookworm/main amd64 libgprofng0 amd64 2.40-2 [812 kB]
2024-01-03T02:30:11.5705276Z #17 2.328 Get:28 http://deb.debian.org/debian bookworm/main amd64 libjansson4 amd64 2.14-2 [40.8 kB]
2024-01-03T02:30:11.5707250Z #17 2.331 Get:29 http://deb.debian.org/debian bookworm/main amd64 binutils-x86-64-linux-gnu amd64 2.40-2 [2246 kB]
2024-01-03T02:30:11.6660906Z #17 2.341 Get:30 http://deb.debian.org/debian bookworm/main amd64 binutils amd64 2.40-2 [65.0 kB]
2024-01-03T02:30:11.6663999Z #17 2.341 Get:31 http://deb.debian.org/debian bookworm/main amd64 libisl23 amd64 0.25-1 [690 kB]
2024-01-03T02:30:11.6666715Z #17 2.344 Get:32 http://deb.debian.org/debian bookworm/main amd64 libmpfr6 amd64 4.2.0-1 [701 kB]
2024-01-03T02:30:11.6667760Z #17 2.348 Get:33 http://deb.debian.org/debian bookworm/main amd64 libmpc3 amd64 1.3.1-1 [51.5 kB]
2024-01-03T02:30:11.6668746Z #17 2.348 Get:34 http://deb.debian.org/debian bookworm/main amd64 cpp-12 amd64 12.2.0-14 [9764 kB]
2024-01-03T02:30:11.6669815Z #17 2.389 Get:35 http://deb.debian.org/debian bookworm/main amd64 cpp amd64 4:12.2.0-3 [6836 B]
2024-01-03T02:30:11.6672391Z #17 2.389 Get:36 http://deb.debian.org/debian bookworm/main amd64 dumb-init amd64 1.2.5-2 [14.1 kB]
2024-01-03T02:30:11.6673639Z #17 2.389 Get:37 http://deb.debian.org/debian bookworm/main amd64 libcc1-0 amd64 12.2.0-14 [41.7 kB]
2024-01-03T02:30:11.6675955Z #17 2.390 Get:38 http://deb.debian.org/debian bookworm/main amd64 libgomp1 amd64 12.2.0-14 [116 kB]
2024-01-03T02:30:11.6677600Z #17 2.391 Get:39 http://deb.debian.org/debian bookworm/main amd64 libitm1 amd64 12.2.0-14 [26.1 kB]
2024-01-03T02:30:11.6680525Z #17 2.391 Get:40 http://deb.debian.org/debian bookworm/main amd64 libatomic1 amd64 12.2.0-14 [9328 B]
2024-01-03T02:30:11.6681537Z #17 2.391 Get:41 http://deb.debian.org/debian bookworm/main amd64 libasan8 amd64 12.2.0-14 [2195 kB]
2024-01-03T02:30:11.6683679Z #17 2.400 Get:42 http://deb.debian.org/debian bookworm/main amd64 liblsan0 amd64 12.2.0-14 [969 kB]
2024-01-03T02:30:11.6684769Z #17 2.404 Get:43 http://deb.debian.org/debian bookworm/main amd64 libtsan2 amd64 12.2.0-14 [2196 kB]
2024-01-03T02:30:11.6685774Z #17 2.413 Get:44 http://deb.debian.org/debian bookworm/main amd64 libubsan1 amd64 12.2.0-14 [883 kB]
2024-01-03T02:30:11.6688269Z #17 2.417 Get:45 http://deb.debian.org/debian bookworm/main amd64 libquadmath0 amd64 12.2.0-14 [144 kB]
2024-01-03T02:30:11.6689597Z #17 2.418 Get:46 http://deb.debian.org/debian bookworm/main amd64 libgcc-12-dev amd64 12.2.0-14 [2437 kB]
2024-01-03T02:30:11.6690628Z #17 2.431 Get:47 http://deb.debian.org/debian bookworm/main amd64 gcc-12 amd64 12.2.0-14 [19.3 MB]
2024-01-03T02:30:12.2325718Z #17 2.905 Get:48 http://deb.debian.org/debian bookworm/main amd64 gcc amd64 4:12.2.0-3 [5216 B]
2024-01-03T02:30:12.2328406Z #17 2.905 Get:49 http://deb.debian.org/debian bookworm/main amd64 libc-dev-bin amd64 2.36-9+deb12u3 [45.2 kB]
2024-01-03T02:30:12.2331886Z #17 2.905 Get:50 http://deb.debian.org/debian-security bookworm-security/main amd64 linux-libc-dev amd64 6.1.69-1 [1910 kB]
2024-01-03T02:30:12.2333874Z #17 2.909 Get:51 http://deb.debian.org/debian bookworm/main amd64 libcrypt-dev amd64 1:4.4.33-2 [118 kB]
2024-01-03T02:30:12.2335993Z #17 2.910 Get:52 http://deb.debian.org/debian bookworm/main amd64 libtirpc-dev amd64 1.3.3+ds-1 [191 kB]
2024-01-03T02:30:12.2337335Z #17 2.911 Get:53 http://deb.debian.org/debian bookworm/main amd64 libnsl-dev amd64 1.3.0-2 [66.4 kB]
2024-01-03T02:30:12.2338818Z #17 2.912 Get:54 http://deb.debian.org/debian bookworm/main amd64 rpcsvc-proto amd64 1.4.3-1 [63.3 kB]
2024-01-03T02:30:12.2340789Z #17 2.912 Get:55 http://deb.debian.org/debian bookworm/main amd64 libc6-dev amd64 2.36-9+deb12u3 [1898 kB]
2024-01-03T02:30:12.2342040Z #17 2.924 Get:56 http://deb.debian.org/debian bookworm/main amd64 libstdc++-12-dev amd64 12.2.0-14 [2046 kB]
2024-01-03T02:30:12.2343618Z #17 2.935 Get:57 http://deb.debian.org/debian bookworm/main amd64 g++-12 amd64 12.2.0-14 [10.7 MB]
2024-01-03T02:30:12.2344885Z #17 2.997 Get:58 http://deb.debian.org/debian bookworm/main amd64 g++ amd64 4:12.2.0-3 [1356 B]
2024-01-03T02:30:12.3423891Z #17 2.998 Get:59 http://deb.debian.org/debian bookworm/main amd64 libnl-3-200 amd64 3.7.0-0.2+b1 [63.1 kB]
2024-01-03T02:30:12.3426595Z #17 2.998 Get:60 http://deb.debian.org/debian bookworm/main amd64 libnl-genl-3-200 amd64 3.7.0-0.2+b1 [21.6 kB]
2024-01-03T02:30:12.3428162Z #17 2.999 Get:61 http://deb.debian.org/debian bookworm/main amd64 htop amd64 3.2.2-2 [152 kB]
2024-01-03T02:30:12.3429248Z #17 2.999 Get:62 http://deb.debian.org/debian bookworm/main amd64 make amd64 4.3-4.1 [396 kB]
2024-01-03T02:30:12.3430174Z #17 3.090 debconf: delaying package configuration, since apt-utils is not installed
2024-01-03T02:30:12.3430848Z #17 3.107 Fetched 73.0 MB in 1s (84.8 MB/s)
2024-01-03T02:30:12.4880681Z #17 3.122 Selecting previously unselected package libssl3:amd64.
2024-01-03T02:30:12.4881818Z #17 3.122 (Reading database ... 
2024-01-03T02:30:12.4882512Z (Reading database ... 5%
2024-01-03T02:30:12.4883148Z (Reading database ... 10%
2024-01-03T02:30:12.4883920Z (Reading database ... 15%
2024-01-03T02:30:12.4884591Z (Reading database ... 20%
2024-01-03T02:30:12.4885077Z (Reading database ... 25%
2024-01-03T02:30:12.4885477Z (Reading database ... 30%
2024-01-03T02:30:12.4885845Z (Reading database ... 35%
2024-01-03T02:30:12.4886274Z (Reading database ... 40%
2024-01-03T02:30:12.4886672Z (Reading database ... 45%
2024-01-03T02:30:12.4887069Z (Reading database ... 50%
2024-01-03T02:30:12.4887791Z (Reading database ... 55%
2024-01-03T02:30:12.4888461Z (Reading database ... 60%
2024-01-03T02:30:12.4889287Z (Reading database ... 65%
2024-01-03T02:30:12.4890019Z (Reading database ... 70%
2024-01-03T02:30:12.4890689Z (Reading database ... 75%
2024-01-03T02:30:12.4891260Z (Reading database ... 80%
2024-01-03T02:30:12.4891693Z (Reading database ... 85%
2024-01-03T02:30:12.4892197Z (Reading database ... 90%
2024-01-03T02:30:12.4892673Z (Reading database ... 95%
2024-01-03T02:30:12.4893136Z (Reading database ... 100%
2024-01-03T02:30:12.4893827Z (Reading database ... 6098 files and directories currently installed.)
2024-01-03T02:30:12.4895201Z #17 3.127 Preparing to unpack .../libssl3_3.0.11-1~deb12u2_amd64.deb ...
2024-01-03T02:30:12.4895914Z #17 3.130 Unpacking libssl3:amd64 (3.0.11-1~deb12u2) ...
2024-01-03T02:30:12.4896968Z #17 3.253 Selecting previously unselected package libpython3.11-minimal:amd64.
2024-01-03T02:30:12.6033057Z #17 3.254 Preparing to unpack .../libpython3.11-minimal_3.11.2-6_amd64.deb ...
2024-01-03T02:30:12.6034012Z #17 3.255 Unpacking libpython3.11-minimal:amd64 (3.11.2-6) ...
2024-01-03T02:30:12.6034866Z #17 3.342 Selecting previously unselected package libexpat1:amd64.
2024-01-03T02:30:12.6035602Z #17 3.343 Preparing to unpack .../libexpat1_2.5.0-1_amd64.deb ...
2024-01-03T02:30:12.6036307Z #17 3.345 Unpacking libexpat1:amd64 (2.5.0-1) ...
2024-01-03T02:30:12.6036997Z #17 3.368 Selecting previously unselected package python3.11-minimal.
2024-01-03T02:30:12.7442945Z #17 3.369 Preparing to unpack .../python3.11-minimal_3.11.2-6_amd64.deb ...
2024-01-03T02:30:12.7444203Z #17 3.373 Unpacking python3.11-minimal (3.11.2-6) ...
2024-01-03T02:30:12.7445277Z #17 3.509 Setting up libssl3:amd64 (3.0.11-1~deb12u2) ...
2024-01-03T02:30:12.8953089Z #17 3.512 Setting up libpython3.11-minimal:amd64 (3.11.2-6) ...
2024-01-03T02:30:12.8954539Z #17 3.517 Setting up libexpat1:amd64 (2.5.0-1) ...
2024-01-03T02:30:12.8955631Z #17 3.520 Setting up python3.11-minimal (3.11.2-6) ...
2024-01-03T02:30:13.3160143Z #17 4.054 Selecting previously unselected package python3-minimal.
2024-01-03T02:30:13.3160920Z #17 4.054 (Reading database ... 
2024-01-03T02:30:13.3161340Z (Reading database ... 5%
2024-01-03T02:30:13.3161855Z (Reading database ... 10%
2024-01-03T02:30:13.3162284Z (Reading database ... 15%
2024-01-03T02:30:13.3162734Z (Reading database ... 20%
2024-01-03T02:30:13.3163100Z (Reading database ... 25%
2024-01-03T02:30:13.3163778Z (Reading database ... 30%
2024-01-03T02:30:13.3164617Z (Reading database ... 35%
2024-01-03T02:30:13.3165344Z (Reading database ... 40%
2024-01-03T02:30:13.3166094Z (Reading database ... 45%
2024-01-03T02:30:13.3166929Z (Reading database ... 50%
2024-01-03T02:30:13.3167392Z (Reading database ... 55%
2024-01-03T02:30:13.3167852Z (Reading database ... 60%
2024-01-03T02:30:13.3168379Z (Reading database ... 65%
2024-01-03T02:30:13.3168753Z (Reading database ... 70%
2024-01-03T02:30:13.3169297Z (Reading database ... 75%
2024-01-03T02:30:13.3169676Z (Reading database ... 80%
2024-01-03T02:30:13.3170100Z (Reading database ... 85%
2024-01-03T02:30:13.3170637Z (Reading database ... 90%
2024-01-03T02:30:13.3171013Z (Reading database ... 95%
2024-01-03T02:30:13.3171465Z (Reading database ... 100%
2024-01-03T02:30:13.3172112Z (Reading database ... 6426 files and directories currently installed.)
2024-01-03T02:30:13.3172975Z #17 4.059 Preparing to unpack .../00-python3-minimal_3.11.2-1+b1_amd64.deb ...
2024-01-03T02:30:13.3173793Z #17 4.061 Unpacking python3-minimal (3.11.2-1+b1) ...
2024-01-03T02:30:13.3174642Z #17 4.081 Selecting previously unselected package media-types.
2024-01-03T02:30:13.4339189Z #17 4.082 Preparing to unpack .../01-media-types_10.0.0_all.deb ...
2024-01-03T02:30:13.4340095Z #17 4.083 Unpacking media-types (10.0.0) ...
2024-01-03T02:30:13.4340971Z #17 4.105 Selecting previously unselected package libncursesw6:amd64.
2024-01-03T02:30:13.4341907Z #17 4.106 Preparing to unpack .../02-libncursesw6_6.4-4_amd64.deb ...
2024-01-03T02:30:13.4342656Z #17 4.107 Unpacking libncursesw6:amd64 (6.4-4) ...
2024-01-03T02:30:13.4343511Z #17 4.132 Selecting previously unselected package libkrb5support0:amd64.
2024-01-03T02:30:13.4344877Z #17 4.133 Preparing to unpack .../03-libkrb5support0_1.20.1-2+deb12u1_amd64.deb ...
2024-01-03T02:30:13.4346424Z #17 4.134 Unpacking libkrb5support0:amd64 (1.20.1-2+deb12u1) ...
2024-01-03T02:30:13.4347625Z #17 4.154 Selecting previously unselected package libk5crypto3:amd64.
2024-01-03T02:30:13.4348838Z #17 4.155 Preparing to unpack .../04-libk5crypto3_1.20.1-2+deb12u1_amd64.deb ...
2024-01-03T02:30:13.4349749Z #17 4.157 Unpacking libk5crypto3:amd64 (1.20.1-2+deb12u1) ...
2024-01-03T02:30:13.4350403Z #17 4.178 Selecting previously unselected package libkeyutils1:amd64.
2024-01-03T02:30:13.4351224Z #17 4.179 Preparing to unpack .../05-libkeyutils1_1.6.3-2_amd64.deb ...
2024-01-03T02:30:13.4352393Z #17 4.180 Unpacking libkeyutils1:amd64 (1.6.3-2) ...
2024-01-03T02:30:13.4353748Z #17 4.199 Selecting previously unselected package libkrb5-3:amd64.
2024-01-03T02:30:13.5490057Z #17 4.200 Preparing to unpack .../06-libkrb5-3_1.20.1-2+deb12u1_amd64.deb ...
2024-01-03T02:30:13.5491252Z #17 4.201 Unpacking libkrb5-3:amd64 (1.20.1-2+deb12u1) ...
2024-01-03T02:30:13.5492130Z #17 4.242 Selecting previously unselected package libgssapi-krb5-2:amd64.
2024-01-03T02:30:13.5492993Z #17 4.243 Preparing to unpack .../07-libgssapi-krb5-2_1.20.1-2+deb12u1_amd64.deb ...
2024-01-03T02:30:13.5493802Z #17 4.245 Unpacking libgssapi-krb5-2:amd64 (1.20.1-2+deb12u1) ...
2024-01-03T02:30:13.5494991Z #17 4.267 Selecting previously unselected package libtirpc-common.
2024-01-03T02:30:13.5495996Z #17 4.268 Preparing to unpack .../08-libtirpc-common_1.3.3+ds-1_all.deb ...
2024-01-03T02:30:13.5497316Z #17 4.269 Unpacking libtirpc-common (1.3.3+ds-1) ...
2024-01-03T02:30:13.5498573Z #17 4.289 Selecting previously unselected package libtirpc3:amd64.
2024-01-03T02:30:13.5499869Z #17 4.289 Preparing to unpack .../09-libtirpc3_1.3.3+ds-1_amd64.deb ...
2024-01-03T02:30:13.5500695Z #17 4.291 Unpacking libtirpc3:amd64 (1.3.3+ds-1) ...
2024-01-03T02:30:13.5501319Z #17 4.314 Selecting previously unselected package libnsl2:amd64.
2024-01-03T02:30:13.6798719Z #17 4.315 Preparing to unpack .../10-libnsl2_1.3.0-2_amd64.deb ...
2024-01-03T02:30:13.6799510Z #17 4.317 Unpacking libnsl2:amd64 (1.3.0-2) ...
2024-01-03T02:30:13.6800276Z #17 4.335 Selecting previously unselected package readline-common.
2024-01-03T02:30:13.6801276Z #17 4.336 Preparing to unpack .../11-readline-common_8.2-1.3_all.deb ...
2024-01-03T02:30:13.6801957Z #17 4.337 Unpacking readline-common (8.2-1.3) ...
2024-01-03T02:30:13.6802665Z #17 4.359 Selecting previously unselected package libreadline8:amd64.
2024-01-03T02:30:13.6803611Z #17 4.359 Preparing to unpack .../12-libreadline8_8.2-1.3_amd64.deb ...
2024-01-03T02:30:13.6804974Z #17 4.361 Unpacking libreadline8:amd64 (8.2-1.3) ...
2024-01-03T02:30:13.6806324Z #17 4.387 Selecting previously unselected package libsqlite3-0:amd64.
2024-01-03T02:30:13.6807340Z #17 4.388 Preparing to unpack .../13-libsqlite3-0_3.40.1-2_amd64.deb ...
2024-01-03T02:30:13.6808163Z #17 4.389 Unpacking libsqlite3-0:amd64 (3.40.1-2) ...
2024-01-03T02:30:13.6808938Z #17 4.445 Selecting previously unselected package libpython3.11-stdlib:amd64.
2024-01-03T02:30:13.8095648Z #17 4.446 Preparing to unpack .../14-libpython3.11-stdlib_3.11.2-6_amd64.deb ...
2024-01-03T02:30:13.8097069Z #17 4.447 Unpacking libpython3.11-stdlib:amd64 (3.11.2-6) ...
2024-01-03T02:30:13.8098003Z #17 4.574 Selecting previously unselected package python3.11.
2024-01-03T02:30:13.9601991Z #17 4.576 Preparing to unpack .../15-python3.11_3.11.2-6_amd64.deb ...
2024-01-03T02:30:13.9603094Z #17 4.577 Unpacking python3.11 (3.11.2-6) ...
2024-01-03T02:30:13.9604134Z #17 4.600 Selecting previously unselected package libpython3-stdlib:amd64.
2024-01-03T02:30:13.9605043Z #17 4.601 Preparing to unpack .../16-libpython3-stdlib_3.11.2-1+b1_amd64.deb ...
2024-01-03T02:30:13.9605873Z #17 4.602 Unpacking libpython3-stdlib:amd64 (3.11.2-1+b1) ...
2024-01-03T02:30:13.9606516Z #17 4.619 Setting up python3-minimal (3.11.2-1+b1) ...
2024-01-03T02:30:14.1112016Z #17 4.732 Selecting previously unselected package python3.
2024-01-03T02:30:14.1113010Z #17 4.732 (Reading database ... 
2024-01-03T02:30:14.1113475Z (Reading database ... 5%
2024-01-03T02:30:14.1113974Z (Reading database ... 10%
2024-01-03T02:30:14.1114370Z (Reading database ... 15%
2024-01-03T02:30:14.1114770Z (Reading database ... 20%
2024-01-03T02:30:14.1115223Z (Reading database ... 25%
2024-01-03T02:30:14.1115614Z (Reading database ... 30%
2024-01-03T02:30:14.1116303Z (Reading database ... 35%
2024-01-03T02:30:14.1116823Z (Reading database ... 40%
2024-01-03T02:30:14.1117237Z (Reading database ... 45%
2024-01-03T02:30:14.1117672Z (Reading database ... 50%
2024-01-03T02:30:14.1118078Z (Reading database ... 55%
2024-01-03T02:30:14.1118470Z (Reading database ... 60%
2024-01-03T02:30:14.1118900Z (Reading database ... 65%
2024-01-03T02:30:14.1119684Z (Reading database ... 70%
2024-01-03T02:30:14.1120058Z (Reading database ... 75%
2024-01-03T02:30:14.1120500Z (Reading database ... 80%
2024-01-03T02:30:14.1120896Z (Reading database ... 85%
2024-01-03T02:30:14.1121330Z (Reading database ... 90%
2024-01-03T02:30:14.1121704Z (Reading database ... 95%
2024-01-03T02:30:14.1122069Z (Reading database ... 100%
2024-01-03T02:30:14.1122675Z (Reading database ... 6934 files and directories currently installed.)
2024-01-03T02:30:14.1123661Z #17 4.736 Preparing to unpack .../00-python3_3.11.2-1+b1_amd64.deb ...
2024-01-03T02:30:14.1124293Z #17 4.740 Unpacking python3 (3.11.2-1+b1) ...
2024-01-03T02:30:14.1125027Z #17 4.757 Selecting previously unselected package binutils-common:amd64.
2024-01-03T02:30:14.1125792Z #17 4.758 Preparing to unpack .../01-binutils-common_2.40-2_amd64.deb ...
2024-01-03T02:30:14.1126823Z #17 4.759 Unpacking binutils-common:amd64 (2.40-2) ...
2024-01-03T02:30:14.2349549Z #17 4.918 Selecting previously unselected package libbinutils:amd64.
2024-01-03T02:30:14.2351040Z #17 4.920 Preparing to unpack .../02-libbinutils_2.40-2_amd64.deb ...
2024-01-03T02:30:14.2351738Z #17 4.921 Unpacking libbinutils:amd64 (2.40-2) ...
2024-01-03T02:30:14.2352510Z #17 4.973 Selecting previously unselected package libctf-nobfd0:amd64.
2024-01-03T02:30:14.2353274Z #17 4.974 Preparing to unpack .../03-libctf-nobfd0_2.40-2_amd64.deb ...
2024-01-03T02:30:14.2353943Z #17 4.975 Unpacking libctf-nobfd0:amd64 (2.40-2) ...
2024-01-03T02:30:14.2354843Z #17 5.000 Selecting previously unselected package libctf0:amd64.
2024-01-03T02:30:14.3459384Z #17 5.001 Preparing to unpack .../04-libctf0_2.40-2_amd64.deb ...
2024-01-03T02:30:14.3460445Z #17 5.002 Unpacking libctf0:amd64 (2.40-2) ...
2024-01-03T02:30:14.3461563Z #17 5.022 Selecting previously unselected package libgprofng0:amd64.
2024-01-03T02:30:14.3462807Z #17 5.023 Preparing to unpack .../05-libgprofng0_2.40-2_amd64.deb ...
2024-01-03T02:30:14.3463949Z #17 5.024 Unpacking libgprofng0:amd64 (2.40-2) ...
2024-01-03T02:30:14.3464993Z #17 5.089 Selecting previously unselected package libjansson4:amd64.
2024-01-03T02:30:14.3466452Z #17 5.090 Preparing to unpack .../06-libjansson4_2.14-2_amd64.deb ...
2024-01-03T02:30:14.3467572Z #17 5.091 Unpacking libjansson4:amd64 (2.14-2) ...
2024-01-03T02:30:14.3468700Z #17 5.111 Selecting previously unselected package binutils-x86-64-linux-gnu.
2024-01-03T02:30:14.4959117Z #17 5.112 Preparing to unpack .../07-binutils-x86-64-linux-gnu_2.40-2_amd64.deb ...
2024-01-03T02:30:14.4960538Z #17 5.114 Unpacking binutils-x86-64-linux-gnu (2.40-2) ...
2024-01-03T02:30:14.5961634Z #17 5.277 Selecting previously unselected package binutils.
2024-01-03T02:30:14.5963024Z #17 5.278 Preparing to unpack .../08-binutils_2.40-2_amd64.deb ...
2024-01-03T02:30:14.5963813Z #17 5.279 Unpacking binutils (2.40-2) ...
2024-01-03T02:30:14.5964387Z #17 5.301 Selecting previously unselected package libisl23:amd64.
2024-01-03T02:30:14.5965084Z #17 5.302 Preparing to unpack .../09-libisl23_0.25-1_amd64.deb ...
2024-01-03T02:30:14.5965807Z #17 5.303 Unpacking libisl23:amd64 (0.25-1) ...
2024-01-03T02:30:14.5966451Z #17 5.360 Selecting previously unselected package libmpfr6:amd64.
2024-01-03T02:30:14.5967217Z #17 5.361 Preparing to unpack .../10-libmpfr6_4.2.0-1_amd64.deb ...
2024-01-03T02:30:14.7466950Z #17 5.363 Unpacking libmpfr6:amd64 (4.2.0-1) ...
2024-01-03T02:30:14.7468041Z #17 5.402 Selecting previously unselected package libmpc3:amd64.
2024-01-03T02:30:14.7469559Z #17 5.403 Preparing to unpack .../11-libmpc3_1.3.1-1_amd64.deb ...
2024-01-03T02:30:14.7470628Z #17 5.404 Unpacking libmpc3:amd64 (1.3.1-1) ...
2024-01-03T02:30:14.7471657Z #17 5.420 Selecting previously unselected package cpp-12.
2024-01-03T02:30:14.7472421Z #17 5.421 Preparing to unpack .../12-cpp-12_12.2.0-14_amd64.deb ...
2024-01-03T02:30:14.7473093Z #17 5.422 Unpacking cpp-12 (12.2.0-14) ...
2024-01-03T02:30:15.1687117Z #17 5.934 Selecting previously unselected package cpp.
2024-01-03T02:30:15.2757363Z #17 5.935 Preparing to unpack .../13-cpp_4%3a12.2.0-3_amd64.deb ...
2024-01-03T02:30:15.2758479Z #17 5.936 Unpacking cpp (4:12.2.0-3) ...
2024-01-03T02:30:15.2759104Z #17 5.951 Selecting previously unselected package dumb-init.
2024-01-03T02:30:15.2759893Z #17 5.952 Preparing to unpack .../14-dumb-init_1.2.5-2_amd64.deb ...
2024-01-03T02:30:15.2760524Z #17 5.953 Unpacking dumb-init (1.2.5-2) ...
2024-01-03T02:30:15.2761541Z #17 5.971 Selecting previously unselected package libcc1-0:amd64.
2024-01-03T02:30:15.2763083Z #17 5.972 Preparing to unpack .../15-libcc1-0_12.2.0-14_amd64.deb ...
2024-01-03T02:30:15.2764199Z #17 5.973 Unpacking libcc1-0:amd64 (12.2.0-14) ...
2024-01-03T02:30:15.2764818Z #17 5.992 Selecting previously unselected package libgomp1:amd64.
2024-01-03T02:30:15.2765696Z #17 5.993 Preparing to unpack .../16-libgomp1_12.2.0-14_amd64.deb ...
2024-01-03T02:30:15.2766341Z #17 5.994 Unpacking libgomp1:amd64 (12.2.0-14) ...
2024-01-03T02:30:15.2766993Z #17 6.020 Selecting previously unselected package libitm1:amd64.
2024-01-03T02:30:15.2767831Z #17 6.020 Preparing to unpack .../17-libitm1_12.2.0-14_amd64.deb ...
2024-01-03T02:30:15.2768463Z #17 6.022 Unpacking libitm1:amd64 (12.2.0-14) ...
2024-01-03T02:30:15.2769135Z #17 6.041 Selecting previously unselected package libatomic1:amd64.
2024-01-03T02:30:15.4258489Z #17 6.041 Preparing to unpack .../18-libatomic1_12.2.0-14_amd64.deb ...
2024-01-03T02:30:15.4259716Z #17 6.043 Unpacking libatomic1:amd64 (12.2.0-14) ...
2024-01-03T02:30:15.4260341Z #17 6.060 Selecting previously unselected package libasan8:amd64.
2024-01-03T02:30:15.4261442Z #17 6.060 Preparing to unpack .../19-libasan8_12.2.0-14_amd64.deb ...
2024-01-03T02:30:15.4262138Z #17 6.062 Unpacking libasan8:amd64 (12.2.0-14) ...
2024-01-03T02:30:15.5261560Z #17 6.215 Selecting previously unselected package liblsan0:amd64.
2024-01-03T02:30:15.5262958Z #17 6.216 Preparing to unpack .../20-liblsan0_12.2.0-14_amd64.deb ...
2024-01-03T02:30:15.5264068Z #17 6.217 Unpacking liblsan0:amd64 (12.2.0-14) ...
2024-01-03T02:30:15.5265067Z #17 6.290 Selecting previously unselected package libtsan2:amd64.
2024-01-03T02:30:15.5266022Z #17 6.291 Preparing to unpack .../21-libtsan2_12.2.0-14_amd64.deb ...
2024-01-03T02:30:15.6766225Z #17 6.292 Unpacking libtsan2:amd64 (12.2.0-14) ...
2024-01-03T02:30:15.7769839Z #17 6.442 Selecting previously unselected package libubsan1:amd64.
2024-01-03T02:30:15.7771190Z #17 6.443 Preparing to unpack .../22-libubsan1_12.2.0-14_amd64.deb ...
2024-01-03T02:30:15.7772466Z #17 6.444 Unpacking libubsan1:amd64 (12.2.0-14) ...
2024-01-03T02:30:15.7773496Z #17 6.514 Selecting previously unselected package libquadmath0:amd64.
2024-01-03T02:30:15.7774871Z #17 6.516 Preparing to unpack .../23-libquadmath0_12.2.0-14_amd64.deb ...
2024-01-03T02:30:15.7776014Z #17 6.517 Unpacking libquadmath0:amd64 (12.2.0-14) ...
2024-01-03T02:30:15.7777317Z #17 6.541 Selecting previously unselected package libgcc-12-dev:amd64.
2024-01-03T02:30:15.7779505Z #17 6.542 Preparing to unpack .../24-libgcc-12-dev_12.2.0-14_amd64.deb ...
2024-01-03T02:30:15.9253940Z #17 6.543 Unpacking libgcc-12-dev:amd64 (12.2.0-14) ...
2024-01-03T02:30:15.9255146Z #17 6.690 Selecting previously unselected package gcc-12.
2024-01-03T02:30:16.0759745Z #17 6.691 Preparing to unpack .../25-gcc-12_12.2.0-14_amd64.deb ...
2024-01-03T02:30:16.0761136Z #17 6.692 Unpacking gcc-12 (12.2.0-14) ...
2024-01-03T02:30:16.6333073Z #17 7.362 Selecting previously unselected package gcc.
2024-01-03T02:30:16.6334221Z #17 7.363 Preparing to unpack .../26-gcc_4%3a12.2.0-3_amd64.deb ...
2024-01-03T02:30:16.6335184Z #17 7.364 Unpacking gcc (4:12.2.0-3) ...
2024-01-03T02:30:16.6335813Z #17 7.380 Selecting previously unselected package libc-dev-bin.
2024-01-03T02:30:16.6336702Z #17 7.381 Preparing to unpack .../27-libc-dev-bin_2.36-9+deb12u3_amd64.deb ...
2024-01-03T02:30:16.6337398Z #17 7.382 Unpacking libc-dev-bin (2.36-9+deb12u3) ...
2024-01-03T02:30:16.6338224Z #17 7.398 Selecting previously unselected package linux-libc-dev:amd64.
2024-01-03T02:30:16.7837385Z #17 7.399 Preparing to unpack .../28-linux-libc-dev_6.1.69-1_amd64.deb ...
2024-01-03T02:30:16.7838704Z #17 7.400 Unpacking linux-libc-dev:amd64 (6.1.69-1) ...
2024-01-03T02:30:16.9017319Z #17 7.585 Selecting previously unselected package libcrypt-dev:amd64.
2024-01-03T02:30:16.9018371Z #17 7.586 Preparing to unpack .../29-libcrypt-dev_1%3a4.4.33-2_amd64.deb ...
2024-01-03T02:30:16.9019099Z #17 7.592 Unpacking libcrypt-dev:amd64 (1:4.4.33-2) ...
2024-01-03T02:30:16.9019842Z #17 7.613 Selecting previously unselected package libtirpc-dev:amd64.
2024-01-03T02:30:16.9020634Z #17 7.615 Preparing to unpack .../30-libtirpc-dev_1.3.3+ds-1_amd64.deb ...
2024-01-03T02:30:16.9021320Z #17 7.616 Unpacking libtirpc-dev:amd64 (1.3.3+ds-1) ...
2024-01-03T02:30:16.9022074Z #17 7.645 Selecting previously unselected package libnsl-dev:amd64.
2024-01-03T02:30:16.9022792Z #17 7.646 Preparing to unpack .../31-libnsl-dev_1.3.0-2_amd64.deb ...
2024-01-03T02:30:16.9023416Z #17 7.647 Unpacking libnsl-dev:amd64 (1.3.0-2) ...
2024-01-03T02:30:16.9024137Z #17 7.667 Selecting previously unselected package rpcsvc-proto.
2024-01-03T02:30:17.0522749Z #17 7.668 Preparing to unpack .../32-rpcsvc-proto_1.4.3-1_amd64.deb ...
2024-01-03T02:30:17.0523664Z #17 7.669 Unpacking rpcsvc-proto (1.4.3-1) ...
2024-01-03T02:30:17.0524408Z #17 7.693 Selecting previously unselected package libc6-dev:amd64.
2024-01-03T02:30:17.0525190Z #17 7.694 Preparing to unpack .../33-libc6-dev_2.36-9+deb12u3_amd64.deb ...
2024-01-03T02:30:17.0526005Z #17 7.695 Unpacking libc6-dev:amd64 (2.36-9+deb12u3) ...
2024-01-03T02:30:17.2027749Z #17 7.840 Selecting previously unselected package libstdc++-12-dev:amd64.
2024-01-03T02:30:17.2028721Z #17 7.841 Preparing to unpack .../34-libstdc++-12-dev_12.2.0-14_amd64.deb ...
2024-01-03T02:30:17.2029460Z #17 7.842 Unpacking libstdc++-12-dev:amd64 (12.2.0-14) ...
2024-01-03T02:30:17.3537532Z #17 8.045 Selecting previously unselected package g++-12.
2024-01-03T02:30:17.3538772Z #17 8.047 Preparing to unpack .../35-g++-12_12.2.0-14_amd64.deb ...
2024-01-03T02:30:17.3539843Z #17 8.048 Unpacking g++-12 (12.2.0-14) ...
2024-01-03T02:30:17.7871306Z #17 8.552 Selecting previously unselected package g++.
2024-01-03T02:30:17.9200598Z #17 8.553 Preparing to unpack .../36-g++_4%3a12.2.0-3_amd64.deb ...
2024-01-03T02:30:17.9201741Z #17 8.555 Unpacking g++ (4:12.2.0-3) ...
2024-01-03T02:30:17.9202724Z #17 8.570 Selecting previously unselected package libnl-3-200:amd64.
2024-01-03T02:30:17.9203529Z #17 8.572 Preparing to unpack .../37-libnl-3-200_3.7.0-0.2+b1_amd64.deb ...
2024-01-03T02:30:17.9204601Z #17 8.573 Unpacking libnl-3-200:amd64 (3.7.0-0.2+b1) ...
2024-01-03T02:30:17.9205871Z #17 8.595 Selecting previously unselected package libnl-genl-3-200:amd64.
2024-01-03T02:30:17.9206959Z #17 8.596 Preparing to unpack .../38-libnl-genl-3-200_3.7.0-0.2+b1_amd64.deb ...
2024-01-03T02:30:17.9207754Z #17 8.597 Unpacking libnl-genl-3-200:amd64 (3.7.0-0.2+b1) ...
2024-01-03T02:30:17.9208456Z #17 8.611 Selecting previously unselected package htop.
2024-01-03T02:30:17.9209108Z #17 8.612 Preparing to unpack .../39-htop_3.2.2-2_amd64.deb ...
2024-01-03T02:30:17.9209966Z #17 8.613 Unpacking htop (3.2.2-2) ...
2024-01-03T02:30:17.9210586Z #17 8.637 Selecting previously unselected package make.
2024-01-03T02:30:17.9211331Z #17 8.638 Preparing to unpack .../40-make_4.3-4.1_amd64.deb ...
2024-01-03T02:30:17.9211989Z #17 8.640 Unpacking make (4.3-4.1) ...
2024-01-03T02:30:17.9212568Z #17 8.685 Setting up media-types (10.0.0) ...
2024-01-03T02:30:18.0280217Z #17 8.691 Setting up dumb-init (1.2.5-2) ...
2024-01-03T02:30:18.0281063Z #17 8.695 Setting up libkeyutils1:amd64 (1.6.3-2) ...
2024-01-03T02:30:18.0281824Z #17 8.710 Setting up libtirpc-common (1.3.3+ds-1) ...
2024-01-03T02:30:18.0282619Z #17 8.714 Setting up libsqlite3-0:amd64 (3.40.1-2) ...
2024-01-03T02:30:18.0283363Z #17 8.717 Setting up binutils-common:amd64 (2.40-2) ...
2024-01-03T02:30:18.0284292Z #17 8.720 Setting up linux-libc-dev:amd64 (6.1.69-1) ...
2024-01-03T02:30:18.0285035Z #17 8.723 Setting up libctf-nobfd0:amd64 (2.40-2) ...
2024-01-03T02:30:18.0286068Z #17 8.726 Setting up libgomp1:amd64 (12.2.0-14) ...
2024-01-03T02:30:18.0286872Z #17 8.731 Setting up libjansson4:amd64 (2.14-2) ...
2024-01-03T02:30:18.0287722Z #17 8.735 Setting up libkrb5support0:amd64 (1.20.1-2+deb12u1) ...
2024-01-03T02:30:18.0288483Z #17 8.738 Setting up rpcsvc-proto (1.4.3-1) ...
2024-01-03T02:30:18.0289206Z #17 8.741 Setting up make (4.3-4.1) ...
2024-01-03T02:30:18.0289953Z #17 8.745 Setting up libmpfr6:amd64 (4.2.0-1) ...
2024-01-03T02:30:18.0290683Z #17 8.749 Setting up libquadmath0:amd64 (12.2.0-14) ...
2024-01-03T02:30:18.0291319Z #17 8.753 Setting up libmpc3:amd64 (1.3.1-1) ...
2024-01-03T02:30:18.0291925Z #17 8.756 Setting up libatomic1:amd64 (12.2.0-14) ...
2024-01-03T02:30:18.0292583Z #17 8.760 Setting up libncursesw6:amd64 (6.4-4) ...
2024-01-03T02:30:18.0293375Z #17 8.763 Setting up libk5crypto3:amd64 (1.20.1-2+deb12u1) ...
2024-01-03T02:30:18.0294126Z #17 8.770 Setting up libubsan1:amd64 (12.2.0-14) ...
2024-01-03T02:30:18.0295222Z #17 8.773 Setting up libcrypt-dev:amd64 (1:4.4.33-2) ...
2024-01-03T02:30:18.0295910Z #17 8.781 Setting up libasan8:amd64 (12.2.0-14) ...
2024-01-03T02:30:18.0296744Z #17 8.784 Setting up libnl-3-200:amd64 (3.7.0-0.2+b1) ...
2024-01-03T02:30:18.0297511Z #17 8.793 Setting up libkrb5-3:amd64 (1.20.1-2+deb12u1) ...
2024-01-03T02:30:18.1300099Z #17 8.796 Setting up libtsan2:amd64 (12.2.0-14) ...
2024-01-03T02:30:18.1301416Z #17 8.799 Setting up libbinutils:amd64 (2.40-2) ...
2024-01-03T02:30:18.1302366Z #17 8.803 Setting up libisl23:amd64 (0.25-1) ...
2024-01-03T02:30:18.1303793Z #17 8.810 Setting up libc-dev-bin (2.36-9+deb12u3) ...
2024-01-03T02:30:18.1304806Z #17 8.817 Setting up readline-common (8.2-1.3) ...
2024-01-03T02:30:18.1305548Z #17 8.822 Setting up libcc1-0:amd64 (12.2.0-14) ...
2024-01-03T02:30:18.1306494Z #17 8.826 Setting up liblsan0:amd64 (12.2.0-14) ...
2024-01-03T02:30:18.1307185Z #17 8.831 Setting up libitm1:amd64 (12.2.0-14) ...
2024-01-03T02:30:18.1307929Z #17 8.834 Setting up libctf0:amd64 (2.40-2) ...
2024-01-03T02:30:18.1308923Z #17 8.837 Setting up cpp-12 (12.2.0-14) ...
2024-01-03T02:30:18.1309651Z #17 8.840 Setting up libreadline8:amd64 (8.2-1.3) ...
2024-01-03T02:30:18.1310686Z #17 8.844 Setting up libgprofng0:amd64 (2.40-2) ...
2024-01-03T02:30:18.1311436Z #17 8.848 Setting up libgcc-12-dev:amd64 (12.2.0-14) ...
2024-01-03T02:30:18.1312276Z #17 8.851 Setting up libgssapi-krb5-2:amd64 (1.20.1-2+deb12u1) ...
2024-01-03T02:30:18.1313324Z #17 8.857 Setting up cpp (4:12.2.0-3) ...
2024-01-03T02:30:18.1314429Z #17 8.864 Setting up libnl-genl-3-200:amd64 (3.7.0-0.2+b1) ...
2024-01-03T02:30:18.1315437Z #17 8.868 Setting up binutils-x86-64-linux-gnu (2.40-2) ...
2024-01-03T02:30:18.1316330Z #17 8.871 Setting up libtirpc3:amd64 (1.3.3+ds-1) ...
2024-01-03T02:30:18.1316979Z #17 8.875 Setting up htop (3.2.2-2) ...
2024-01-03T02:30:18.1317993Z #17 8.879 Setting up binutils (2.40-2) ...
2024-01-03T02:30:18.1319092Z #17 8.882 Setting up libtirpc-dev:amd64 (1.3.3+ds-1) ...
2024-01-03T02:30:18.1319928Z #17 8.886 Setting up gcc-12 (12.2.0-14) ...
2024-01-03T02:30:18.1320601Z #17 8.891 Setting up libnsl2:amd64 (1.3.0-2) ...
2024-01-03T02:30:18.1321395Z #17 8.895 Setting up libpython3.11-stdlib:amd64 (3.11.2-6) ...
2024-01-03T02:30:18.2809708Z #17 8.899 Setting up gcc (4:12.2.0-3) ...
2024-01-03T02:30:18.2810503Z #17 8.908 Setting up libnsl-dev:amd64 (1.3.0-2) ...
2024-01-03T02:30:18.2811163Z #17 8.911 Setting up libc6-dev:amd64 (2.36-9+deb12u3) ...
2024-01-03T02:30:18.2811828Z #17 8.914 Setting up libpython3-stdlib:amd64 (3.11.2-1+b1) ...
2024-01-03T02:30:18.2812535Z #17 8.918 Setting up python3.11 (3.11.2-6) ...
2024-01-03T02:30:18.7085981Z #17 9.473 Setting up libstdc++-12-dev:amd64 (12.2.0-14) ...
2024-01-03T02:30:18.8592365Z #17 9.477 Setting up python3 (3.11.2-1+b1) ...
2024-01-03T02:30:18.8593013Z #17 9.553 Setting up g++-12 (12.2.0-14) ...
2024-01-03T02:30:18.8593536Z #17 9.557 Setting up g++ (4:12.2.0-3) ...
2024-01-03T02:30:18.8594534Z #17 9.562 update-alternatives: using /usr/bin/g++ to provide /usr/bin/c++ (c++) in auto mode
2024-01-03T02:30:18.8595750Z #17 9.564 Processing triggers for libc-bin (2.36-9+deb12u3) ...
2024-01-03T02:30:19.5761951Z #17 DONE 10.3s
2024-01-03T02:30:19.7266221Z 
2024-01-03T02:30:19.7267333Z #18 [stage-0  8/12] COPY package-lock.json .
2024-01-03T02:30:19.7267885Z #18 DONE 0.0s
2024-01-03T02:30:19.7268104Z 
2024-01-03T02:30:19.7268337Z #19 [stage-0  9/12] COPY package.json .
2024-01-03T02:30:19.7268841Z #19 DONE 0.0s
2024-01-03T02:30:19.7269046Z 
2024-01-03T02:30:19.7269373Z #20 [stage-0 10/12] RUN --mount=type=cache,target=/root/.cache npm ci
2024-01-03T02:30:31.5999917Z #20 11.91 
2024-01-03T02:30:31.6000782Z #20 11.91 added 965 packages, and audited 966 packages in 11s
2024-01-03T02:30:31.6001882Z #20 11.91 
2024-01-03T02:30:31.6002500Z #20 11.91 184 packages are looking for funding
2024-01-03T02:30:31.6003298Z #20 11.91   run `npm fund` for details
2024-01-03T02:30:31.6004118Z #20 11.91 
2024-01-03T02:30:31.6004634Z #20 11.91 found 0 vulnerabilities
2024-01-03T02:30:31.6005243Z #20 11.91 npm notice 
2024-01-03T02:30:31.6006346Z #20 11.91 npm notice New patch version of npm available! 10.2.3 -> 10.2.5
2024-01-03T02:30:31.6007420Z #20 11.91 npm notice Changelog: <https://github.com/npm/cli/releases/tag/v10.2.5>
2024-01-03T02:30:31.6008693Z #20 11.91 npm notice Run `npm install -g npm@10.2.5` to update!
2024-01-03T02:30:31.6009247Z #20 11.91 npm notice 
2024-01-03T02:30:32.3459114Z #20 DONE 12.6s
2024-01-03T02:30:32.3459507Z 
2024-01-03T02:30:32.3460024Z #21 [stage-0 11/12] COPY . .
2024-01-03T02:30:32.3460887Z #21 DONE 0.1s
2024-01-03T02:30:32.4960083Z 
2024-01-03T02:30:32.4961465Z #22 [stage-0 12/12] RUN npm run build
2024-01-03T02:30:32.9475080Z #22 0.475 
2024-01-03T02:30:32.9476077Z #22 0.475 > skellybot@0.0.1 build
2024-01-03T02:30:32.9477199Z #22 0.475 > nest build
2024-01-03T02:30:32.9478050Z #22 0.475 
2024-01-03T02:30:36.9682164Z #22 4.621 npm notice 
2024-01-03T02:30:37.1182630Z #22 4.621 npm notice New patch version of npm available! 10.2.3 -> 10.2.5
2024-01-03T02:30:37.1184378Z #22 4.622 npm notice Changelog: <https://github.com/npm/cli/releases/tag/v10.2.5>
2024-01-03T02:30:37.1185778Z #22 4.622 npm notice Run `npm install -g npm@10.2.5` to update!
2024-01-03T02:30:37.1186669Z #22 4.622 npm notice 
2024-01-03T02:30:37.2689489Z #22 DONE 4.8s
2024-01-03T02:30:37.2689927Z 
2024-01-03T02:30:37.2690212Z #23 exporting to image
2024-01-03T02:30:37.2691019Z #23 exporting layers
2024-01-03T02:30:43.3245715Z #23 exporting layers 6.2s done
2024-01-03T02:30:43.3247146Z #23 writing image sha256:fcad9b030154424a2b2ef4aaf843bea06bdaeebd1be0eb6e3fc2d1e086e697fc done
2024-01-03T02:30:43.3249902Z #23 naming to us-east1-docker.pkg.dev/mocap-test-project/jonbot/nestbot:676f2b55cf418a17d13170730d6e74fdec198dea done
2024-01-03T02:30:43.3251507Z #23 DONE 6.2s
2024-01-03T02:30:43.4431887Z #0 building with "default" instance using docker driver
2024-01-03T02:30:43.4432444Z 
2024-01-03T02:30:43.4432693Z #1 [internal] load build definition from Dockerfile
2024-01-03T02:30:43.5888020Z #1 transferring dockerfile: 1.03kB done
2024-01-03T02:30:43.5889153Z #1 DONE 0.0s
2024-01-03T02:30:43.5890060Z 
2024-01-03T02:30:43.5890333Z #2 [internal] load .dockerignore
2024-01-03T02:30:43.5890981Z #2 transferring context: 57B done
2024-01-03T02:30:43.5891551Z #2 DONE 0.0s
2024-01-03T02:30:43.5891850Z 
2024-01-03T02:30:43.5892091Z #3 resolve image config for docker.io/docker/dockerfile:1.2
2024-01-03T02:30:43.5892786Z #3 DONE 0.1s
2024-01-03T02:30:43.7390948Z 
2024-01-03T02:30:43.7395052Z #4 docker-image://docker.io/docker/dockerfile:1.2@sha256:e2a8561e419ab1ba6b2fe6cbdf49fd92b95912df1cf7d313c3e2230a333fdbcc
2024-01-03T02:30:43.7396004Z #4 CACHED
2024-01-03T02:30:43.7396179Z 
2024-01-03T02:30:43.7396415Z #5 [internal] load build definition from Dockerfile
2024-01-03T02:30:43.7396997Z #5 DONE 0.0s
2024-01-03T02:30:43.7397195Z 
2024-01-03T02:30:43.7397382Z #6 [internal] load .dockerignore
2024-01-03T02:30:43.7397781Z #6 DONE 0.0s
2024-01-03T02:30:43.7398062Z 
2024-01-03T02:30:43.7398395Z #7 [internal] load metadata for docker.io/library/node:20.10.0-slim
2024-01-03T02:30:43.8367683Z #7 DONE 0.1s
2024-01-03T02:30:43.8368583Z 
2024-01-03T02:30:43.8369818Z #8 [stage-0  1/12] FROM docker.io/library/node:20.10.0-slim@sha256:5c714c3e90f66a2cbfa266b90a4d7adcd63453cd730aa2d13cba84b260bea2e6
2024-01-03T02:30:43.8370983Z #8 DONE 0.0s
2024-01-03T02:30:43.8371240Z 
2024-01-03T02:30:43.8371392Z #9 [internal] load build context
2024-01-03T02:30:43.8372060Z #9 transferring context: 13.84kB 0.0s done
2024-01-03T02:30:43.8372533Z #9 DONE 0.0s
2024-01-03T02:30:43.8372741Z 
2024-01-03T02:30:43.8373521Z #10 [stage-0  6/12] RUN useradd -m appuser && chown -R appuser /workspace && chown -R appuser "/home/.npm"
2024-01-03T02:30:43.8374459Z #10 CACHED
2024-01-03T02:30:43.8374736Z 
2024-01-03T02:30:43.8375519Z #11 [stage-0  5/12] RUN mkdir /home/.npm
2024-01-03T02:30:43.8376346Z #11 CACHED
2024-01-03T02:30:43.8376540Z 
2024-01-03T02:30:43.8376798Z #12 [stage-0  9/12] COPY package.json .
2024-01-03T02:30:43.8377300Z #12 CACHED
2024-01-03T02:30:43.8377479Z 
2024-01-03T02:30:43.8378044Z #13 [stage-0  3/12] RUN rm -rf /etc/apt/apt.conf.d/docker-clean
2024-01-03T02:30:43.8378566Z #13 CACHED
2024-01-03T02:30:43.8378729Z 
2024-01-03T02:30:43.8379020Z #14 [stage-0  2/12] WORKDIR /workspace
2024-01-03T02:30:43.8379670Z #14 CACHED
2024-01-03T02:30:43.8379843Z 
2024-01-03T02:30:43.8380217Z #15 [stage-0 10/12] RUN --mount=type=cache,target=/root/.cache npm ci
2024-01-03T02:30:43.8381023Z #15 CACHED
2024-01-03T02:30:43.8381295Z 
2024-01-03T02:30:43.8381572Z #16 [stage-0  4/12] COPY ./bin/builds/ .
2024-01-03T02:30:43.8382161Z #16 CACHED
2024-01-03T02:30:43.8382643Z 
2024-01-03T02:30:43.8382882Z #17 [stage-0 11/12] COPY . .
2024-01-03T02:30:43.8383270Z #17 CACHED
2024-01-03T02:30:43.8383558Z 
2024-01-03T02:30:43.8383921Z #18 [stage-0  8/12] COPY package-lock.json .
2024-01-03T02:30:43.8384378Z #18 CACHED
2024-01-03T02:30:43.8384570Z 
2024-01-03T02:30:43.8385475Z #19 [stage-0  7/12] RUN --mount=type=cache,target=/var/cache/apt ./install_packages     dumb-init     htop     make     g++     python3
2024-01-03T02:30:43.8386368Z #19 CACHED
2024-01-03T02:30:43.8386671Z 
2024-01-03T02:30:43.8386977Z #20 [stage-0 12/12] RUN npm run build
2024-01-03T02:30:43.8387486Z #20 CACHED
2024-01-03T02:30:43.8387683Z 
2024-01-03T02:30:43.8387837Z #21 exporting to image
2024-01-03T02:30:43.8388319Z #21 exporting layers done
2024-01-03T02:30:43.8389051Z #21 writing image sha256:fcad9b030154424a2b2ef4aaf843bea06bdaeebd1be0eb6e3fc2d1e086e697fc done
2024-01-03T02:30:43.8390018Z #21 naming to us-east1-docker.pkg.dev/mocap-test-project/jonbot/nestbot:latest done
2024-01-03T02:30:43.8390663Z #21 DONE 0.0s
2024-01-03T02:30:43.8560248Z The push refers to repository [us-east1-docker.pkg.dev/mocap-test-project/jonbot/nestbot]
2024-01-03T02:30:43.9494529Z b3c7467259e9: Preparing
2024-01-03T02:30:43.9496059Z 12ab71e11763: Preparing
2024-01-03T02:30:43.9497578Z 313da2cc0709: Preparing
2024-01-03T02:30:43.9498277Z d840ddb0de9a: Preparing
2024-01-03T02:30:43.9498789Z 34253bbb8c56: Preparing
2024-01-03T02:30:43.9499326Z 6271da7e1db8: Preparing
2024-01-03T02:30:43.9499754Z 9670a0129a94: Preparing
2024-01-03T02:30:43.9500223Z 0328c4df6e44: Preparing
2024-01-03T02:30:43.9500617Z c8cfecd17c73: Preparing
2024-01-03T02:30:43.9501021Z 950f606bdab1: Preparing
2024-01-03T02:30:43.9501471Z 6a031daedbbe: Preparing
2024-01-03T02:30:43.9501872Z 54670042a040: Preparing
2024-01-03T02:30:43.9502249Z 0d1064329154: Preparing
2024-01-03T02:30:43.9502694Z e15f668bdea1: Preparing
2024-01-03T02:30:43.9503089Z 6a02db9fb904: Preparing
2024-01-03T02:30:43.9503549Z 7292cf786aa8: Preparing
2024-01-03T02:30:43.9503958Z 6a031daedbbe: Waiting
2024-01-03T02:30:43.9504334Z 54670042a040: Waiting
2024-01-03T02:30:43.9504761Z 0d1064329154: Waiting
2024-01-03T02:30:43.9505146Z 6271da7e1db8: Waiting
2024-01-03T02:30:43.9505514Z e15f668bdea1: Waiting
2024-01-03T02:30:43.9505958Z 0328c4df6e44: Waiting
2024-01-03T02:30:43.9506326Z 6a02db9fb904: Waiting
2024-01-03T02:30:43.9506772Z c8cfecd17c73: Waiting
2024-01-03T02:30:43.9507171Z 950f606bdab1: Waiting
2024-01-03T02:30:43.9507880Z 7292cf786aa8: Waiting
2024-01-03T02:30:45.0313896Z b3c7467259e9: Pushed
2024-01-03T02:30:45.1450946Z d840ddb0de9a: Pushed
2024-01-03T02:30:45.1989674Z 34253bbb8c56: Pushed
2024-01-03T02:30:45.7720953Z 12ab71e11763: Pushed
2024-01-03T02:30:46.1308044Z 0328c4df6e44: Pushed
2024-01-03T02:30:46.1814740Z 9670a0129a94: Pushed
2024-01-03T02:30:46.7934038Z c8cfecd17c73: Pushed
2024-01-03T02:30:47.0204569Z 950f606bdab1: Pushed
2024-01-03T02:30:47.0251144Z 54670042a040: Layer already exists
2024-01-03T02:30:47.1681270Z 6a031daedbbe: Pushed
2024-01-03T02:30:47.2268368Z 0d1064329154: Layer already exists
2024-01-03T02:30:47.2527835Z e15f668bdea1: Layer already exists
2024-01-03T02:30:47.3745251Z 6a02db9fb904: Layer already exists
2024-01-03T02:30:47.4337072Z 7292cf786aa8: Layer already exists
2024-01-03T02:30:56.8346275Z 313da2cc0709: Pushed
2024-01-03T02:30:57.9080286Z 6271da7e1db8: Pushed
2024-01-03T02:30:59.2323388Z 676f2b55cf418a17d13170730d6e74fdec198dea: digest: sha256:7cf5b50013cbf99a0d6d0029452297a06ad259fd23a26abf9b9153ebf71a391c size: 3666
2024-01-03T02:30:59.2482346Z The push refers to repository [us-east1-docker.pkg.dev/mocap-test-project/jonbot/nestbot]
2024-01-03T02:30:59.4425353Z b3c7467259e9: Preparing
2024-01-03T02:30:59.4426403Z 12ab71e11763: Preparing
2024-01-03T02:30:59.4429974Z 313da2cc0709: Preparing
2024-01-03T02:30:59.4430735Z d840ddb0de9a: Preparing
2024-01-03T02:30:59.4431774Z 34253bbb8c56: Preparing
2024-01-03T02:30:59.4433694Z 6271da7e1db8: Preparing
2024-01-03T02:30:59.4434610Z 9670a0129a94: Preparing
2024-01-03T02:30:59.4435547Z 0328c4df6e44: Preparing
2024-01-03T02:30:59.4436074Z 6271da7e1db8: Waiting
2024-01-03T02:30:59.4436433Z 9670a0129a94: Waiting
2024-01-03T02:30:59.4436853Z c8cfecd17c73: Preparing
2024-01-03T02:30:59.4437232Z 0328c4df6e44: Waiting
2024-01-03T02:30:59.4437582Z 950f606bdab1: Preparing
2024-01-03T02:30:59.4438026Z 6a031daedbbe: Preparing
2024-01-03T02:30:59.4438446Z 950f606bdab1: Waiting
2024-01-03T02:30:59.4438801Z c8cfecd17c73: Waiting
2024-01-03T02:30:59.4439240Z 54670042a040: Preparing
2024-01-03T02:30:59.4439596Z 0d1064329154: Preparing
2024-01-03T02:30:59.4440028Z e15f668bdea1: Preparing
2024-01-03T02:30:59.4440390Z 6a031daedbbe: Waiting
2024-01-03T02:30:59.4440738Z 54670042a040: Waiting
2024-01-03T02:30:59.4441147Z 0d1064329154: Waiting
2024-01-03T02:30:59.4441484Z e15f668bdea1: Waiting
2024-01-03T02:30:59.4441848Z 6a02db9fb904: Preparing
2024-01-03T02:30:59.4442279Z 7292cf786aa8: Preparing
2024-01-03T02:30:59.4442697Z 6a02db9fb904: Waiting
2024-01-03T02:30:59.4443122Z 7292cf786aa8: Waiting
2024-01-03T02:30:59.6509965Z 34253bbb8c56: Layer already exists
2024-01-03T02:30:59.6562794Z 12ab71e11763: Layer already exists
2024-01-03T02:30:59.6592060Z 313da2cc0709: Layer already exists
2024-01-03T02:30:59.6656912Z d840ddb0de9a: Layer already exists
2024-01-03T02:30:59.6673084Z b3c7467259e9: Layer already exists
2024-01-03T02:30:59.7563627Z 6271da7e1db8: Layer already exists
2024-01-03T02:30:59.7667718Z 9670a0129a94: Layer already exists
2024-01-03T02:30:59.7704560Z 950f606bdab1: Layer already exists
2024-01-03T02:30:59.7838503Z c8cfecd17c73: Layer already exists
2024-01-03T02:30:59.8605798Z 0328c4df6e44: Layer already exists
2024-01-03T02:30:59.8692309Z 6a031daedbbe: Layer already exists
2024-01-03T02:30:59.8736243Z 54670042a040: Layer already exists
2024-01-03T02:30:59.8806532Z 0d1064329154: Layer already exists
2024-01-03T02:30:59.8900470Z e15f668bdea1: Layer already exists
2024-01-03T02:30:59.9711499Z 7292cf786aa8: Layer already exists
2024-01-03T02:31:00.0690343Z 6a02db9fb904: Layer already exists
2024-01-03T02:31:00.4210699Z latest: digest: sha256:7cf5b50013cbf99a0d6d0029452297a06ad259fd23a26abf9b9153ebf71a391c size: 3666
2024-01-03T02:31:00.4265744Z ##[group]Run gcloud compute instances stop skelly-bot-testing --zone=us-central1-a
2024-01-03T02:31:00.4266773Z [36;1mgcloud compute instances stop skelly-bot-testing --zone=us-central1-a[0m
2024-01-03T02:31:00.4267567Z [36;1mgcloud compute instances start skelly-bot-testing --zone=us-central1-a[0m
2024-01-03T02:31:00.4317697Z shell: /usr/bin/bash -e {0}
2024-01-03T02:31:00.4318199Z env:
2024-01-03T02:31:00.4318537Z   PROJECT_ID: mocap-test-project
2024-01-03T02:31:00.4318976Z   GAR_LOCATION: us-east1
2024-01-03T02:31:00.4319418Z   SERVICE: jonbot/nestbot
2024-01-03T02:31:00.4319808Z   REGION: us-central1
2024-01-03T02:31:00.4320560Z   CLOUDSDK_AUTH_CREDENTIAL_FILE_OVERRIDE: /home/runner/work/skellybot/skellybot/gha-creds-4199cb2c73bcb4f5.json
2024-01-03T02:31:00.4321588Z   GOOGLE_APPLICATION_CREDENTIALS: /home/runner/work/skellybot/skellybot/gha-creds-4199cb2c73bcb4f5.json
2024-01-03T02:31:00.4322715Z   GOOGLE_GHA_CREDS_PATH: /home/runner/work/skellybot/skellybot/gha-creds-4199cb2c73bcb4f5.json
2024-01-03T02:31:00.4323437Z   CLOUDSDK_CORE_PROJECT: mocap-test-project
2024-01-03T02:31:00.4323907Z   CLOUDSDK_PROJECT: mocap-test-project
2024-01-03T02:31:00.4324397Z   GCLOUD_PROJECT: mocap-test-project
2024-01-03T02:31:00.4324851Z   GCP_PROJECT: mocap-test-project
2024-01-03T02:31:00.4325289Z   GOOGLE_CLOUD_PROJECT: mocap-test-project
2024-01-03T02:31:00.4325830Z ##[endgroup]
2024-01-03T02:31:03.6585667Z Stopping instance(s) skelly-bot-testing...
2024-01-03T02:31:44.6515602Z ............................................................................................................................................................................................................done.
2024-01-03T02:31:44.9291442Z Updated [https://compute.googleapis.com/compute/v1/projects/mocap-test-project/zones/us-central1-a/instances/skelly-bot-testing].
2024-01-03T02:31:46.8311906Z Starting instance(s) skelly-bot-testing...
2024-01-03T02:31:54.6366630Z ......................................done.
2024-01-03T02:31:54.8501558Z Updated [https://compute.googleapis.com/compute/v1/projects/mocap-test-project/zones/us-central1-a/instances/skelly-bot-testing].
2024-01-03T02:31:54.8502636Z Instance internal IP is 10.128.0.10
2024-01-03T02:31:54.8503152Z Instance external IP is 34.121.144.57
2024-01-03T02:31:54.9884792Z ##[group]Run echo 
2024-01-03T02:31:54.9885213Z [36;1mecho [0m
2024-01-03T02:31:54.9934739Z shell: /usr/bin/bash -e {0}
2024-01-03T02:31:54.9935230Z env:
2024-01-03T02:31:54.9935582Z   PROJECT_ID: mocap-test-project
2024-01-03T02:31:54.9936064Z   GAR_LOCATION: us-east1
2024-01-03T02:31:54.9936437Z   SERVICE: jonbot/nestbot
2024-01-03T02:31:54.9936821Z   REGION: us-central1
2024-01-03T02:31:54.9937567Z   CLOUDSDK_AUTH_CREDENTIAL_FILE_OVERRIDE: /home/runner/work/skellybot/skellybot/gha-creds-4199cb2c73bcb4f5.json
2024-01-03T02:31:54.9938627Z   GOOGLE_APPLICATION_CREDENTIALS: /home/runner/work/skellybot/skellybot/gha-creds-4199cb2c73bcb4f5.json
2024-01-03T02:31:54.9939574Z   GOOGLE_GHA_CREDS_PATH: /home/runner/work/skellybot/skellybot/gha-creds-4199cb2c73bcb4f5.json
2024-01-03T02:31:54.9940332Z   CLOUDSDK_CORE_PROJECT: mocap-test-project
2024-01-03T02:31:54.9940824Z   CLOUDSDK_PROJECT: mocap-test-project
2024-01-03T02:31:54.9941327Z   GCLOUD_PROJECT: mocap-test-project
2024-01-03T02:31:54.9941872Z   GCP_PROJECT: mocap-test-project
2024-01-03T02:31:54.9942371Z   GOOGLE_CLOUD_PROJECT: mocap-test-project
2024-01-03T02:31:54.9942818Z ##[endgroup]
2024-01-03T02:31:55.0011357Z 
2024-01-03T02:31:55.0060976Z Post job cleanup.
2024-01-03T02:31:55.1085031Z [command]/usr/bin/docker logout us-east1-docker.pkg.dev
2024-01-03T02:31:55.1214109Z Removing login credentials for us-east1-docker.pkg.dev
2024-01-03T02:31:55.1364579Z Post job cleanup.
2024-01-03T02:31:55.2173201Z Removed exported credentials at "/home/runner/work/skellybot/skellybot/gha-creds-4199cb2c73bcb4f5.json".
2024-01-03T02:31:55.2351423Z Post job cleanup.
2024-01-03T02:31:55.3073758Z [command]/usr/bin/git version
2024-01-03T02:31:55.3112919Z git version 2.43.0
2024-01-03T02:31:55.3152984Z Temporarily overriding HOME='/home/runner/work/_temp/89f7f647-03ee-4d9e-ae84-652bbade38be' before making global git config changes
2024-01-03T02:31:55.3154758Z Adding repository directory to the temporary git global config as a safe directory
2024-01-03T02:31:55.3157716Z [command]/usr/bin/git config --global --add safe.directory /home/runner/work/skellybot/skellybot
2024-01-03T02:31:55.3190684Z [command]/usr/bin/git config --local --name-only --get-regexp core\.sshCommand
2024-01-03T02:31:55.3222848Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"
2024-01-03T02:31:55.3464574Z [command]/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
2024-01-03T02:31:55.3484548Z http.https://github.com/.extraheader
2024-01-03T02:31:55.3495448Z [command]/usr/bin/git config --local --unset-all http.https://github.com/.extraheader
2024-01-03T02:31:55.3526290Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :"
2024-01-03T02:31:55.3993020Z Cleaning up orphan processes

LOGS FROM A WORKING DEPLOYMENT END
+++++++




============

LOGS FROM A NON-WORKING BROKEN DEPLOYMENT START
2024-01-13T13:47:48.3457417Z Requested labels: ubuntu-latest
2024-01-13T13:47:48.3457696Z Job defined at: freemocap/skellybot/.github/workflows/google-cloudrun-docker.yml@refs/heads/main
2024-01-13T13:47:48.3457804Z Waiting for a runner to pick up this job...
2024-01-13T13:47:48.9332094Z Job is waiting for a hosted runner to come online.
2024-01-13T13:47:52.5032737Z Job is about to start running on the hosted runner: GitHub Actions 3 (hosted)
2024-01-13T13:47:54.4111317Z Current runner version: '2.311.0'
2024-01-13T13:47:54.4140774Z ##[group]Operating System
2024-01-13T13:47:54.4141424Z Ubuntu
2024-01-13T13:47:54.4141924Z 22.04.3
2024-01-13T13:47:54.4142262Z LTS
2024-01-13T13:47:54.4142572Z ##[endgroup]
2024-01-13T13:47:54.4143049Z ##[group]Runner Image
2024-01-13T13:47:54.4143492Z Image: ubuntu-22.04
2024-01-13T13:47:54.4143989Z Version: 20240107.1.0
2024-01-13T13:47:54.4144993Z Included Software: https://github.com/actions/runner-images/blob/ubuntu22/20240107.1/images/ubuntu/Ubuntu2204-Readme.md
2024-01-13T13:47:54.4146445Z Image Release: https://github.com/actions/runner-images/releases/tag/ubuntu22%2F20240107.1
2024-01-13T13:47:54.4147362Z ##[endgroup]
2024-01-13T13:47:54.4147769Z ##[group]Runner Image Provisioner
2024-01-13T13:47:54.4148281Z 2.0.321.1
2024-01-13T13:47:54.4148708Z ##[endgroup]
2024-01-13T13:47:54.4149561Z ##[group]GITHUB_TOKEN Permissions
2024-01-13T13:47:54.4151206Z Contents: read
2024-01-13T13:47:54.4151652Z Metadata: read
2024-01-13T13:47:54.4152295Z ##[endgroup]
2024-01-13T13:47:54.4155287Z Secret source: Actions
2024-01-13T13:47:54.4155880Z Prepare workflow directory
2024-01-13T13:47:54.4874038Z Prepare all required actions
2024-01-13T13:47:54.5030123Z Getting action download info
2024-01-13T13:47:54.7486774Z Download action repository 'actions/checkout@v4' (SHA:b4ffde65f46336ab88eb53be808477a3936bae11)
2024-01-13T13:47:54.8588707Z Download action repository 'google-github-actions/auth@v2' (SHA:f6de81663f7788d05bd15bcce18f0e57f23f0846)
2024-01-13T13:47:55.1150613Z Download action repository 'docker/login-action@v3' (SHA:343f7c4344506bcbf9b4de18042ae17996df046d)
2024-01-13T13:47:55.4649531Z Complete job name: deploy
2024-01-13T13:47:55.5547979Z ##[group]Run actions/checkout@v4
2024-01-13T13:47:55.5548494Z with:
2024-01-13T13:47:55.5548981Z   repository: freemocap/skellybot
2024-01-13T13:47:55.5549590Z   token: ***
2024-01-13T13:47:55.5549914Z   ssh-strict: true
2024-01-13T13:47:55.5550428Z   persist-credentials: true
2024-01-13T13:47:55.5550815Z   clean: true
2024-01-13T13:47:55.5551275Z   sparse-checkout-cone-mode: true
2024-01-13T13:47:55.5551687Z   fetch-depth: 1
2024-01-13T13:47:55.5552019Z   fetch-tags: false
2024-01-13T13:47:55.5552421Z   show-progress: true
2024-01-13T13:47:55.5552779Z   lfs: false
2024-01-13T13:47:55.5553092Z   submodules: false
2024-01-13T13:47:55.5553545Z   set-safe-directory: true
2024-01-13T13:47:55.5553919Z env:
2024-01-13T13:47:55.5554210Z   PROJECT_ID: mocap-test-project
2024-01-13T13:47:55.5554726Z   GAR_LOCATION: us-east1
2024-01-13T13:47:55.5555097Z   SERVICE: jonbot/nestbot
2024-01-13T13:47:55.5555480Z   REGION: us-central1
2024-01-13T13:47:55.5555892Z ##[endgroup]
2024-01-13T13:47:55.7287562Z Syncing repository: freemocap/skellybot
2024-01-13T13:47:55.7289754Z ##[group]Getting Git version info
2024-01-13T13:47:55.7290480Z Working directory is '/home/runner/work/skellybot/skellybot'
2024-01-13T13:47:55.7291567Z [command]/usr/bin/git version
2024-01-13T13:47:55.7309265Z git version 2.43.0
2024-01-13T13:47:55.7333858Z ##[endgroup]
2024-01-13T13:47:55.7355362Z Temporarily overriding HOME='/home/runner/work/_temp/c0cbb21b-53a2-47a3-8f7d-eb2549f25acb' before making global git config changes
2024-01-13T13:47:55.7357571Z Adding repository directory to the temporary git global config as a safe directory
2024-01-13T13:47:55.7359469Z [command]/usr/bin/git config --global --add safe.directory /home/runner/work/skellybot/skellybot
2024-01-13T13:47:55.7394165Z Deleting the contents of '/home/runner/work/skellybot/skellybot'
2024-01-13T13:47:55.7401633Z ##[group]Initializing the repository
2024-01-13T13:47:55.7404812Z [command]/usr/bin/git init /home/runner/work/skellybot/skellybot
2024-01-13T13:47:55.7494020Z hint: Using 'master' as the name for the initial branch. This default branch name
2024-01-13T13:47:55.7495408Z hint: is subject to change. To configure the initial branch name to use in all
2024-01-13T13:47:55.7496823Z hint: of your new repositories, which will suppress this warning, call:
2024-01-13T13:47:55.7497859Z hint: 
2024-01-13T13:47:55.7498654Z hint: 	git config --global init.defaultBranch <name>
2024-01-13T13:47:55.7499245Z hint: 
2024-01-13T13:47:55.7499770Z hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
2024-01-13T13:47:55.7500681Z hint: 'development'. The just-created branch can be renamed via this command:
2024-01-13T13:47:55.7501370Z hint: 
2024-01-13T13:47:55.7501729Z hint: 	git branch -m <name>
2024-01-13T13:47:55.7505252Z Initialized empty Git repository in /home/runner/work/skellybot/skellybot/.git/
2024-01-13T13:47:55.7513964Z [command]/usr/bin/git remote add origin https://github.com/freemocap/skellybot
2024-01-13T13:47:55.7548770Z ##[endgroup]
2024-01-13T13:47:55.7549560Z ##[group]Disabling automatic garbage collection
2024-01-13T13:47:55.7551293Z [command]/usr/bin/git config --local gc.auto 0
2024-01-13T13:47:55.7580385Z ##[endgroup]
2024-01-13T13:47:55.7580995Z ##[group]Setting up auth
2024-01-13T13:47:55.7585297Z [command]/usr/bin/git config --local --name-only --get-regexp core\.sshCommand
2024-01-13T13:47:55.7614242Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"
2024-01-13T13:47:55.7945945Z [command]/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
2024-01-13T13:47:55.7973151Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :"
2024-01-13T13:47:55.8202227Z [command]/usr/bin/git config --local http.https://github.com/.extraheader AUTHORIZATION: basic ***
2024-01-13T13:47:55.8264254Z ##[endgroup]
2024-01-13T13:47:55.8266691Z ##[group]Fetching the repository
2024-01-13T13:47:55.8275121Z [command]/usr/bin/git -c protocol.version=2 fetch --no-tags --prune --no-recurse-submodules --depth=1 origin +042e1b9eee40ab55edabb9a9e4e8f6d36b3f6da0:refs/remotes/origin/main
2024-01-13T13:47:56.1846251Z From https://github.com/freemocap/skellybot
2024-01-13T13:47:56.1847723Z  * [new ref]         042e1b9eee40ab55edabb9a9e4e8f6d36b3f6da0 -> origin/main
2024-01-13T13:47:56.1873601Z ##[endgroup]
2024-01-13T13:47:56.1874342Z ##[group]Determining the checkout info
2024-01-13T13:47:56.1875732Z ##[endgroup]
2024-01-13T13:47:56.1876506Z ##[group]Checking out the ref
2024-01-13T13:47:56.1880326Z [command]/usr/bin/git checkout --progress --force -B main refs/remotes/origin/main
2024-01-13T13:47:56.2548957Z Switched to a new branch 'main'
2024-01-13T13:47:56.2550411Z branch 'main' set up to track 'origin/main'.
2024-01-13T13:47:56.2559281Z ##[endgroup]
2024-01-13T13:47:56.2593672Z [command]/usr/bin/git log -1 --format='%H'
2024-01-13T13:47:56.2617393Z '042e1b9eee40ab55edabb9a9e4e8f6d36b3f6da0'
2024-01-13T13:47:56.2931867Z ##[group]Run google-github-actions/auth@v2
2024-01-13T13:47:56.2932335Z with:
2024-01-13T13:47:56.2932697Z   project_id: mocap-test-project
2024-01-13T13:47:56.2933224Z   token_format: access_token
2024-01-13T13:47:56.2934181Z   workload_identity_provider: ***
2024-01-13T13:47:56.2934813Z   service_account: ***
2024-01-13T13:47:56.2935260Z   create_credentials_file: true
2024-01-13T13:47:56.2935680Z   export_environment_variables: true
2024-01-13T13:47:56.2936170Z   universe: googleapis.com
2024-01-13T13:47:56.2936517Z   cleanup_credentials: true
2024-01-13T13:47:56.2936917Z   access_token_lifetime: 3600s
2024-01-13T13:47:56.2937751Z   access_token_scopes: https://www.googleapis.com/auth/cloud-platform
2024-01-13T13:47:56.2938378Z   retries: 3
2024-01-13T13:47:56.2938703Z   backoff: 250
2024-01-13T13:47:56.2939130Z   id_token_include_email: false
2024-01-13T13:47:56.2939493Z env:
2024-01-13T13:47:56.2939817Z   PROJECT_ID: mocap-test-project
2024-01-13T13:47:56.2940386Z   GAR_LOCATION: us-east1
2024-01-13T13:47:56.2940752Z   SERVICE: jonbot/nestbot
2024-01-13T13:47:56.2941138Z   REGION: us-central1
2024-01-13T13:47:56.2941495Z ##[endgroup]
2024-01-13T13:47:56.4798884Z Created credentials file at "/home/runner/work/skellybot/skellybot/gha-creds-51ca75be46286648.json"
2024-01-13T13:47:56.6710710Z ##[group]Run docker/login-action@v3
2024-01-13T13:47:56.6711293Z with:
2024-01-13T13:47:56.6711671Z   username: oauth2accesstoken
2024-01-13T13:47:56.6717246Z   password: ***
2024-01-13T13:47:56.6717650Z   registry: us-east1-docker.pkg.dev
2024-01-13T13:47:56.6718066Z   ecr: auto
2024-01-13T13:47:56.6718455Z   logout: true
2024-01-13T13:47:56.6718791Z env:
2024-01-13T13:47:56.6719183Z   PROJECT_ID: mocap-test-project
2024-01-13T13:47:56.6719613Z   GAR_LOCATION: us-east1
2024-01-13T13:47:56.6719982Z   SERVICE: jonbot/nestbot
2024-01-13T13:47:56.6720445Z   REGION: us-central1
2024-01-13T13:47:56.6721170Z   CLOUDSDK_AUTH_CREDENTIAL_FILE_OVERRIDE: /home/runner/work/skellybot/skellybot/gha-creds-51ca75be46286648.json
2024-01-13T13:47:56.6722853Z   GOOGLE_APPLICATION_CREDENTIALS: /home/runner/work/skellybot/skellybot/gha-creds-51ca75be46286648.json
2024-01-13T13:47:56.6723942Z   GOOGLE_GHA_CREDS_PATH: /home/runner/work/skellybot/skellybot/gha-creds-51ca75be46286648.json
2024-01-13T13:47:56.6724880Z   CLOUDSDK_CORE_PROJECT: mocap-test-project
2024-01-13T13:47:56.6725379Z   CLOUDSDK_PROJECT: mocap-test-project
2024-01-13T13:47:56.6725885Z   GCLOUD_PROJECT: mocap-test-project
2024-01-13T13:47:56.6726342Z   GCP_PROJECT: mocap-test-project
2024-01-13T13:47:56.6726781Z   GOOGLE_CLOUD_PROJECT: mocap-test-project
2024-01-13T13:47:56.6727274Z ##[endgroup]
2024-01-13T13:47:56.7729543Z Logging into us-east1-docker.pkg.dev...
2024-01-13T13:47:57.3057049Z Login Succeeded!
2024-01-13T13:47:57.3172116Z ##[group]Run docker build -t "us-east1-docker.pkg.dev/mocap-test-project/jonbot/nestbot:042e1b9eee40ab55edabb9a9e4e8f6d36b3f6da0" ./
2024-01-13T13:47:57.3173604Z [36;1mdocker build -t "us-east1-docker.pkg.dev/mocap-test-project/jonbot/nestbot:042e1b9eee40ab55edabb9a9e4e8f6d36b3f6da0" ./[0m
2024-01-13T13:47:57.3174859Z [36;1mdocker build -t "us-east1-docker.pkg.dev/mocap-test-project/jonbot/nestbot:latest" ./[0m
2024-01-13T13:47:57.3175956Z [36;1mdocker push "us-east1-docker.pkg.dev/mocap-test-project/jonbot/nestbot:042e1b9eee40ab55edabb9a9e4e8f6d36b3f6da0"[0m
2024-01-13T13:47:57.3177082Z [36;1mdocker push "us-east1-docker.pkg.dev/mocap-test-project/jonbot/nestbot:latest"[0m
2024-01-13T13:47:57.3241833Z shell: /usr/bin/bash -e {0}
2024-01-13T13:47:57.3242260Z env:
2024-01-13T13:47:57.3242622Z   PROJECT_ID: mocap-test-project
2024-01-13T13:47:57.3243131Z   GAR_LOCATION: us-east1
2024-01-13T13:47:57.3243524Z   SERVICE: jonbot/nestbot
2024-01-13T13:47:57.3244067Z   REGION: us-central1
2024-01-13T13:47:57.3244767Z   CLOUDSDK_AUTH_CREDENTIAL_FILE_OVERRIDE: /home/runner/work/skellybot/skellybot/gha-creds-51ca75be46286648.json
2024-01-13T13:47:57.3245788Z   GOOGLE_APPLICATION_CREDENTIALS: /home/runner/work/skellybot/skellybot/gha-creds-51ca75be46286648.json
2024-01-13T13:47:57.3246808Z   GOOGLE_GHA_CREDS_PATH: /home/runner/work/skellybot/skellybot/gha-creds-51ca75be46286648.json
2024-01-13T13:47:57.3247517Z   CLOUDSDK_CORE_PROJECT: mocap-test-project
2024-01-13T13:47:57.3248077Z   CLOUDSDK_PROJECT: mocap-test-project
2024-01-13T13:47:57.3248533Z   GCLOUD_PROJECT: mocap-test-project
2024-01-13T13:47:57.3248964Z   GCP_PROJECT: mocap-test-project
2024-01-13T13:47:57.3249547Z   GOOGLE_CLOUD_PROJECT: mocap-test-project
2024-01-13T13:47:57.3249991Z ##[endgroup]
2024-01-13T13:47:57.8577761Z #0 building with "default" instance using docker driver
2024-01-13T13:47:57.8578572Z 
2024-01-13T13:47:57.8579451Z #1 [internal] load .dockerignore
2024-01-13T13:47:57.8580462Z #1 transferring context: 57B done
2024-01-13T13:47:57.8580888Z #1 DONE 0.0s
2024-01-13T13:47:57.8581484Z 
2024-01-13T13:47:57.8581919Z #2 [internal] load build definition from Dockerfile
2024-01-13T13:47:57.8582735Z #2 transferring dockerfile: 1.03kB done
2024-01-13T13:47:57.8584049Z #2 DONE 0.0s
2024-01-13T13:47:57.8584350Z 
2024-01-13T13:47:57.8585082Z #3 [auth] docker/dockerfile:pull token for registry-1.docker.io
2024-01-13T13:47:57.8585732Z #3 DONE 0.0s
2024-01-13T13:47:57.8586361Z 
2024-01-13T13:47:57.8586609Z #4 resolve image config for docker.io/docker/dockerfile:1.2
2024-01-13T13:47:58.1583404Z #4 DONE 0.4s
2024-01-13T13:47:58.1584997Z 
2024-01-13T13:47:58.1587293Z #5 docker-image://docker.io/docker/dockerfile:1.2@sha256:e2a8561e419ab1ba6b2fe6cbdf49fd92b95912df1cf7d313c3e2230a333fdbcc
2024-01-13T13:47:58.1589417Z #5 resolve docker.io/docker/dockerfile:1.2@sha256:e2a8561e419ab1ba6b2fe6cbdf49fd92b95912df1cf7d313c3e2230a333fdbcc done
2024-01-13T13:47:58.3018404Z #5 sha256:e2a8561e419ab1ba6b2fe6cbdf49fd92b95912df1cf7d313c3e2230a333fdbcc 1.69kB / 1.69kB done
2024-01-13T13:47:58.3019736Z #5 sha256:e3ee2e6b536452d876b1c5aa12db9bca51b8f52b2505178cae6d13e33daeed2b 528B / 528B done
2024-01-13T13:47:58.3021249Z #5 sha256:86e43bba076d67c1a890cbc07813806b11eca53843dc643202d939b986c8c332 1.21kB / 1.21kB done
2024-01-13T13:47:58.3022636Z #5 sha256:3cc8e449ce9f6e0752ede8f50a7334bf0c7b2d24d76da2ffae7aa6a729dd1da4 9.64MB / 9.64MB 0.1s done
2024-01-13T13:47:58.3024054Z #5 extracting sha256:3cc8e449ce9f6e0752ede8f50a7334bf0c7b2d24d76da2ffae7aa6a729dd1da4
2024-01-13T13:47:58.4155870Z #5 extracting sha256:3cc8e449ce9f6e0752ede8f50a7334bf0c7b2d24d76da2ffae7aa6a729dd1da4 0.1s done
2024-01-13T13:47:58.4156987Z #5 DONE 0.2s
2024-01-13T13:47:58.4157306Z 
2024-01-13T13:47:58.4157603Z #6 [internal] load .dockerignore
2024-01-13T13:47:58.4158282Z #6 DONE 0.0s
2024-01-13T13:47:58.4158780Z 
2024-01-13T13:47:58.4159110Z #7 [internal] load build definition from Dockerfile
2024-01-13T13:47:58.4159982Z #7 DONE 0.0s
2024-01-13T13:47:58.4160330Z 
2024-01-13T13:47:58.4161565Z #8 [internal] load metadata for docker.io/library/node:20.10.0-slim
2024-01-13T13:47:58.5665507Z #8 ...
2024-01-13T13:47:58.5665887Z 
2024-01-13T13:47:58.5666440Z #9 [auth] library/node:pull token for registry-1.docker.io
2024-01-13T13:47:58.5666978Z #9 DONE 0.0s
2024-01-13T13:47:58.7027994Z 
2024-01-13T13:47:58.7029141Z #8 [internal] load metadata for docker.io/library/node:20.10.0-slim
2024-01-13T13:47:58.7030051Z #8 DONE 0.3s
2024-01-13T13:47:58.8531950Z 
2024-01-13T13:47:58.8534299Z #10 [stage-0  1/12] FROM docker.io/library/node:20.10.0-slim@sha256:5c714c3e90f66a2cbfa266b90a4d7adcd63453cd730aa2d13cba84b260bea2e6
2024-01-13T13:47:58.8536722Z #10 resolve docker.io/library/node:20.10.0-slim@sha256:5c714c3e90f66a2cbfa266b90a4d7adcd63453cd730aa2d13cba84b260bea2e6 done
2024-01-13T13:47:58.9708093Z #10 sha256:e21beee6f6d33b4605828c995958d12a7fb3762621c15d3c4355bfed122a11f0 2.67MB / 2.67MB 0.2s done
2024-01-13T13:47:58.9710065Z #10 sha256:5c714c3e90f66a2cbfa266b90a4d7adcd63453cd730aa2d13cba84b260bea2e6 1.21kB / 1.21kB done
2024-01-13T13:47:58.9711560Z #10 sha256:df49e2dc50b7b1f91b44201432cefaf034f66e549bcbd3a29745ffff439afc9e 1.37kB / 1.37kB done
2024-01-13T13:47:58.9713126Z #10 sha256:03f4750834334638efe8f99b5b6c69c08048988fe711078c6889d536dc88aea1 7.62kB / 7.62kB done
2024-01-13T13:47:58.9714862Z #10 sha256:af107e978371b6cd6339127a05502c5eacd1e6b0e9eb7b2f4aa7b6fc87e2dd81 20.97MB / 29.13MB 0.2s
2024-01-13T13:47:58.9716512Z #10 sha256:ebd7ac832a7e4bd07f5ad6f4bbc6db1f5b02de7a8e07b40627142ef61a9b1b9d 3.36kB / 3.36kB 0.1s done
2024-01-13T13:47:58.9718270Z #10 sha256:c5da3822f0fa5def8cc49ddb050ab51e134b313fe72ac31489d0303587f27281 12.58MB / 40.46MB 0.2s
2024-01-13T13:47:58.9719946Z #10 sha256:6e2165efc3a7fb15942e607201f825c49ec4b664e3988e01e2e4a78b682da50e 0B / 451B 0.2s
2024-01-13T13:47:59.1213827Z #10 ...
2024-01-13T13:47:59.1214257Z 
2024-01-13T13:47:59.1214686Z #11 [internal] load build context
2024-01-13T13:47:59.1215439Z #11 transferring context: 19.82MB 0.2s done
2024-01-13T13:47:59.1216192Z #11 DONE 0.2s
2024-01-13T13:47:59.1216629Z 
2024-01-13T13:47:59.1219451Z #10 [stage-0  1/12] FROM docker.io/library/node:20.10.0-slim@sha256:5c714c3e90f66a2cbfa266b90a4d7adcd63453cd730aa2d13cba84b260bea2e6
2024-01-13T13:47:59.1221388Z #10 sha256:af107e978371b6cd6339127a05502c5eacd1e6b0e9eb7b2f4aa7b6fc87e2dd81 29.13MB / 29.13MB 0.3s done
2024-01-13T13:47:59.1223016Z #10 sha256:c5da3822f0fa5def8cc49ddb050ab51e134b313fe72ac31489d0303587f27281 22.02MB / 40.46MB 0.3s
2024-01-13T13:47:59.1225023Z #10 sha256:6e2165efc3a7fb15942e607201f825c49ec4b664e3988e01e2e4a78b682da50e 451B / 451B 0.2s done
2024-01-13T13:47:59.1226575Z #10 extracting sha256:af107e978371b6cd6339127a05502c5eacd1e6b0e9eb7b2f4aa7b6fc87e2dd81
2024-01-13T13:47:59.2703707Z #10 sha256:c5da3822f0fa5def8cc49ddb050ab51e134b313fe72ac31489d0303587f27281 40.46MB / 40.46MB 0.5s
2024-01-13T13:47:59.3852491Z #10 sha256:c5da3822f0fa5def8cc49ddb050ab51e134b313fe72ac31489d0303587f27281 40.46MB / 40.46MB 0.5s done
2024-01-13T13:48:00.2254536Z #10 extracting sha256:af107e978371b6cd6339127a05502c5eacd1e6b0e9eb7b2f4aa7b6fc87e2dd81 1.0s done
2024-01-13T13:48:00.2256202Z #10 extracting sha256:ebd7ac832a7e4bd07f5ad6f4bbc6db1f5b02de7a8e07b40627142ef61a9b1b9d done
2024-01-13T13:48:00.3757423Z #10 extracting sha256:c5da3822f0fa5def8cc49ddb050ab51e134b313fe72ac31489d0303587f27281
2024-01-13T13:48:01.6080618Z #10 extracting sha256:c5da3822f0fa5def8cc49ddb050ab51e134b313fe72ac31489d0303587f27281 1.2s done
2024-01-13T13:48:01.7371423Z #10 extracting sha256:e21beee6f6d33b4605828c995958d12a7fb3762621c15d3c4355bfed122a11f0 0.1s done
2024-01-13T13:48:01.8882005Z #10 extracting sha256:6e2165efc3a7fb15942e607201f825c49ec4b664e3988e01e2e4a78b682da50e done
2024-01-13T13:48:01.8883600Z #10 DONE 3.0s
2024-01-13T13:48:01.8884240Z 
2024-01-13T13:48:01.8887850Z #12 [stage-0  2/12] WORKDIR /workspace
2024-01-13T13:48:01.8888999Z #12 DONE 0.0s
2024-01-13T13:48:01.8889482Z 
2024-01-13T13:48:01.8890199Z #13 [stage-0  3/12] RUN rm -rf /etc/apt/apt.conf.d/docker-clean
2024-01-13T13:48:01.9970733Z #13 DONE 0.2s
2024-01-13T13:48:01.9971488Z 
2024-01-13T13:48:01.9972253Z #14 [stage-0  4/12] COPY ./bin/builds/ .
2024-01-13T13:48:01.9973232Z #14 DONE 0.0s
2024-01-13T13:48:02.1480953Z 
2024-01-13T13:48:02.2877511Z #15 [stage-0  5/12] RUN mkdir /home/.npm
2024-01-13T13:48:02.2878726Z #15 DONE 0.3s
2024-01-13T13:48:02.4378454Z 
2024-01-13T13:48:02.4380058Z #16 [stage-0  6/12] RUN useradd -m appuser && chown -R appuser /workspace && chown -R appuser "/home/.npm"
2024-01-13T13:48:02.5469001Z #16 DONE 0.3s
2024-01-13T13:48:02.6973232Z 
2024-01-13T13:48:02.6976521Z #17 [stage-0  7/12] RUN --mount=type=cache,target=/var/cache/apt ./install_packages     dumb-init     htop     make     g++     python3
2024-01-13T13:48:04.3334156Z #17 1.635 Reading package lists...
2024-01-13T13:48:04.3335177Z #17 1.645 Building dependency tree...
2024-01-13T13:48:04.3335887Z #17 1.724 Reading state information...
2024-01-13T13:48:04.4844191Z #17 1.815 The following additional packages will be installed:
2024-01-13T13:48:04.4845832Z #17 1.815   binutils binutils-common binutils-x86-64-linux-gnu cpp cpp-12 g++-12 gcc
2024-01-13T13:48:04.4846963Z #17 1.815   gcc-12 libasan8 libatomic1 libbinutils libc-dev-bin libc6-dev libcc1-0
2024-01-13T13:48:04.4847995Z #17 1.815   libcrypt-dev libctf-nobfd0 libctf0 libexpat1 libgcc-12-dev libgomp1
2024-01-13T13:48:04.4848866Z #17 1.816   libgprofng0 libgssapi-krb5-2 libisl23 libitm1 libjansson4 libk5crypto3
2024-01-13T13:48:04.4849811Z #17 1.816   libkeyutils1 libkrb5-3 libkrb5support0 liblsan0 libmpc3 libmpfr6
2024-01-13T13:48:04.4850625Z #17 1.816   libncursesw6 libnl-3-200 libnl-genl-3-200 libnsl-dev libnsl2
2024-01-13T13:48:04.4851480Z #17 1.816   libpython3-stdlib libpython3.11-minimal libpython3.11-stdlib libquadmath0
2024-01-13T13:48:04.4852491Z #17 1.816   libreadline8 libsqlite3-0 libssl3 libstdc++-12-dev libtirpc-common
2024-01-13T13:48:04.4853347Z #17 1.816   libtirpc-dev libtirpc3 libtsan2 libubsan1 linux-libc-dev media-types
2024-01-13T13:48:04.4854336Z #17 1.816   python3-minimal python3.11 python3.11-minimal readline-common rpcsvc-proto
2024-01-13T13:48:04.4854996Z #17 1.817 Suggested packages:
2024-01-13T13:48:04.4855685Z #17 1.817   binutils-doc cpp-doc gcc-12-locales cpp-12-doc g++-multilib g++-12-multilib
2024-01-13T13:48:04.4856648Z #17 1.817   gcc-12-doc gcc-multilib manpages-dev autoconf automake libtool flex bison
2024-01-13T13:48:04.4857831Z #17 1.817   gdb gcc-doc gcc-12-multilib lm-sensors lsof strace glibc-doc krb5-doc
2024-01-13T13:48:04.4859432Z #17 1.817   krb5-user libstdc++-12-doc make-doc python3-doc python3-tk python3-venv
2024-01-13T13:48:04.4860381Z #17 1.817   python3.11-venv python3.11-doc binfmt-support readline-doc
2024-01-13T13:48:04.4860959Z #17 1.817 Recommended packages:
2024-01-13T13:48:04.4861696Z #17 1.817   manpages manpages-dev libc-devtools krb5-locales libgpm2 ca-certificates
2024-01-13T13:48:04.6114699Z #17 2.064 The following NEW packages will be installed:
2024-01-13T13:48:04.7622872Z #17 2.064   binutils binutils-common binutils-x86-64-linux-gnu cpp cpp-12 dumb-init g++
2024-01-13T13:48:04.7623979Z #17 2.064   g++-12 gcc gcc-12 htop libasan8 libatomic1 libbinutils libc-dev-bin
2024-01-13T13:48:04.7624839Z #17 2.064   libc6-dev libcc1-0 libcrypt-dev libctf-nobfd0 libctf0 libexpat1
2024-01-13T13:48:04.7625792Z #17 2.065   libgcc-12-dev libgomp1 libgprofng0 libgssapi-krb5-2 libisl23 libitm1
2024-01-13T13:48:04.7626674Z #17 2.065   libjansson4 libk5crypto3 libkeyutils1 libkrb5-3 libkrb5support0 liblsan0
2024-01-13T13:48:04.7627612Z #17 2.065   libmpc3 libmpfr6 libncursesw6 libnl-3-200 libnl-genl-3-200 libnsl-dev
2024-01-13T13:48:04.7628530Z #17 2.065   libnsl2 libpython3-stdlib libpython3.11-minimal libpython3.11-stdlib
2024-01-13T13:48:04.7629396Z #17 2.065   libquadmath0 libreadline8 libsqlite3-0 libssl3 libstdc++-12-dev
2024-01-13T13:48:04.7630303Z #17 2.065   libtirpc-common libtirpc-dev libtirpc3 libtsan2 libubsan1 linux-libc-dev
2024-01-13T13:48:04.7631193Z #17 2.065   make media-types python3 python3-minimal python3.11 python3.11-minimal
2024-01-13T13:48:04.7632146Z #17 2.066   readline-common rpcsvc-proto
2024-01-13T13:48:05.0264722Z #17 2.440 0 upgraded, 62 newly installed, 0 to remove and 0 not upgraded.
2024-01-13T13:48:05.0267288Z #17 2.440 Need to get 73.0 MB of archives.
2024-01-13T13:48:05.0268102Z #17 2.440 After this operation, 294 MB of additional disk space will be used.
2024-01-13T13:48:05.0270833Z #17 2.440 Get:1 http://deb.debian.org/debian bookworm/main amd64 libssl3 amd64 3.0.11-1~deb12u2 [2019 kB]
2024-01-13T13:48:05.0272284Z #17 2.479 Get:2 http://deb.debian.org/debian bookworm/main amd64 libpython3.11-minimal amd64 3.11.2-6 [813 kB]
2024-01-13T13:48:05.1452244Z #17 2.483 Get:3 http://deb.debian.org/debian bookworm/main amd64 libexpat1 amd64 2.5.0-1 [99.3 kB]
2024-01-13T13:48:05.1455439Z #17 2.483 Get:4 http://deb.debian.org/debian bookworm/main amd64 python3.11-minimal amd64 3.11.2-6 [2064 kB]
2024-01-13T13:48:05.1457870Z #17 2.491 Get:5 http://deb.debian.org/debian bookworm/main amd64 python3-minimal amd64 3.11.2-1+b1 [26.3 kB]
2024-01-13T13:48:05.1459689Z #17 2.492 Get:6 http://deb.debian.org/debian bookworm/main amd64 media-types all 10.0.0 [26.1 kB]
2024-01-13T13:48:05.1461609Z #17 2.492 Get:7 http://deb.debian.org/debian bookworm/main amd64 libncursesw6 amd64 6.4-4 [134 kB]
2024-01-13T13:48:05.1463074Z #17 2.493 Get:8 http://deb.debian.org/debian bookworm/main amd64 libkrb5support0 amd64 1.20.1-2+deb12u1 [32.4 kB]
2024-01-13T13:48:05.1465387Z #17 2.493 Get:9 http://deb.debian.org/debian bookworm/main amd64 libk5crypto3 amd64 1.20.1-2+deb12u1 [78.9 kB]
2024-01-13T13:48:05.1467513Z #17 2.494 Get:10 http://deb.debian.org/debian bookworm/main amd64 libkeyutils1 amd64 1.6.3-2 [8808 B]
2024-01-13T13:48:05.1469510Z #17 2.494 Get:11 http://deb.debian.org/debian bookworm/main amd64 libkrb5-3 amd64 1.20.1-2+deb12u1 [332 kB]
2024-01-13T13:48:05.1471773Z #17 2.496 Get:12 http://deb.debian.org/debian bookworm/main amd64 libgssapi-krb5-2 amd64 1.20.1-2+deb12u1 [134 kB]
2024-01-13T13:48:05.1473484Z #17 2.496 Get:13 http://deb.debian.org/debian bookworm/main amd64 libtirpc-common all 1.3.3+ds-1 [14.0 kB]
2024-01-13T13:48:05.1475081Z #17 2.499 Get:14 http://deb.debian.org/debian bookworm/main amd64 libtirpc3 amd64 1.3.3+ds-1 [85.2 kB]
2024-01-13T13:48:05.1476488Z #17 2.500 Get:15 http://deb.debian.org/debian bookworm/main amd64 libnsl2 amd64 1.3.0-2 [39.5 kB]
2024-01-13T13:48:05.1477902Z #17 2.500 Get:16 http://deb.debian.org/debian bookworm/main amd64 readline-common all 8.2-1.3 [69.0 kB]
2024-01-13T13:48:05.1479302Z #17 2.505 Get:17 http://deb.debian.org/debian bookworm/main amd64 libreadline8 amd64 8.2-1.3 [166 kB]
2024-01-13T13:48:05.1480369Z #17 2.507 Get:18 http://deb.debian.org/debian bookworm/main amd64 libsqlite3-0 amd64 3.40.1-2 [837 kB]
2024-01-13T13:48:05.1481441Z #17 2.511 Get:19 http://deb.debian.org/debian bookworm/main amd64 libpython3.11-stdlib amd64 3.11.2-6 [1796 kB]
2024-01-13T13:48:05.1482592Z #17 2.519 Get:20 http://deb.debian.org/debian bookworm/main amd64 python3.11 amd64 3.11.2-6 [572 kB]
2024-01-13T13:48:05.1483686Z #17 2.521 Get:21 http://deb.debian.org/debian bookworm/main amd64 libpython3-stdlib amd64 3.11.2-1+b1 [9312 B]
2024-01-13T13:48:05.1484736Z #17 2.522 Get:22 http://deb.debian.org/debian bookworm/main amd64 python3 amd64 3.11.2-1+b1 [26.3 kB]
2024-01-13T13:48:05.1485868Z #17 2.522 Get:23 http://deb.debian.org/debian bookworm/main amd64 binutils-common amd64 2.40-2 [2487 kB]
2024-01-13T13:48:05.1486915Z #17 2.533 Get:24 http://deb.debian.org/debian bookworm/main amd64 libbinutils amd64 2.40-2 [572 kB]
2024-01-13T13:48:05.1487985Z #17 2.535 Get:25 http://deb.debian.org/debian bookworm/main amd64 libctf-nobfd0 amd64 2.40-2 [153 kB]
2024-01-13T13:48:05.1488995Z #17 2.536 Get:26 http://deb.debian.org/debian bookworm/main amd64 libctf0 amd64 2.40-2 [89.8 kB]
2024-01-13T13:48:05.1489963Z #17 2.537 Get:27 http://deb.debian.org/debian bookworm/main amd64 libgprofng0 amd64 2.40-2 [812 kB]
2024-01-13T13:48:05.1491037Z #17 2.540 Get:28 http://deb.debian.org/debian bookworm/main amd64 libjansson4 amd64 2.14-2 [40.8 kB]
2024-01-13T13:48:05.1492256Z #17 2.541 Get:29 http://deb.debian.org/debian bookworm/main amd64 binutils-x86-64-linux-gnu amd64 2.40-2 [2246 kB]
2024-01-13T13:48:05.1493432Z #17 2.551 Get:30 http://deb.debian.org/debian bookworm/main amd64 binutils amd64 2.40-2 [65.0 kB]
2024-01-13T13:48:05.1494401Z #17 2.551 Get:31 http://deb.debian.org/debian bookworm/main amd64 libisl23 amd64 0.25-1 [690 kB]
2024-01-13T13:48:05.1495355Z #17 2.554 Get:32 http://deb.debian.org/debian bookworm/main amd64 libmpfr6 amd64 4.2.0-1 [701 kB]
2024-01-13T13:48:05.1496394Z #17 2.557 Get:33 http://deb.debian.org/debian bookworm/main amd64 libmpc3 amd64 1.3.1-1 [51.5 kB]
2024-01-13T13:48:05.1497343Z #17 2.558 Get:34 http://deb.debian.org/debian bookworm/main amd64 cpp-12 amd64 12.2.0-14 [9764 kB]
2024-01-13T13:48:05.1498564Z #17 2.598 Get:35 http://deb.debian.org/debian bookworm/main amd64 cpp amd64 4:12.2.0-3 [6836 B]
2024-01-13T13:48:05.2658922Z #17 2.598 Get:36 http://deb.debian.org/debian bookworm/main amd64 dumb-init amd64 1.2.5-2 [14.1 kB]
2024-01-13T13:48:05.2661221Z #17 2.598 Get:37 http://deb.debian.org/debian bookworm/main amd64 libcc1-0 amd64 12.2.0-14 [41.7 kB]
2024-01-13T13:48:05.2663021Z #17 2.599 Get:38 http://deb.debian.org/debian bookworm/main amd64 libgomp1 amd64 12.2.0-14 [116 kB]
2024-01-13T13:48:05.2665494Z #17 2.599 Get:39 http://deb.debian.org/debian bookworm/main amd64 libitm1 amd64 12.2.0-14 [26.1 kB]
2024-01-13T13:48:05.2666680Z #17 2.600 Get:40 http://deb.debian.org/debian bookworm/main amd64 libatomic1 amd64 12.2.0-14 [9328 B]
2024-01-13T13:48:05.2667875Z #17 2.600 Get:41 http://deb.debian.org/debian bookworm/main amd64 libasan8 amd64 12.2.0-14 [2195 kB]
2024-01-13T13:48:05.2668962Z #17 2.610 Get:42 http://deb.debian.org/debian bookworm/main amd64 liblsan0 amd64 12.2.0-14 [969 kB]
2024-01-13T13:48:05.2670016Z #17 2.614 Get:43 http://deb.debian.org/debian bookworm/main amd64 libtsan2 amd64 12.2.0-14 [2196 kB]
2024-01-13T13:48:05.2671147Z #17 2.623 Get:44 http://deb.debian.org/debian bookworm/main amd64 libubsan1 amd64 12.2.0-14 [883 kB]
2024-01-13T13:48:05.2672292Z #17 2.627 Get:45 http://deb.debian.org/debian bookworm/main amd64 libquadmath0 amd64 12.2.0-14 [144 kB]
2024-01-13T13:48:05.2673404Z #17 2.628 Get:46 http://deb.debian.org/debian bookworm/main amd64 libgcc-12-dev amd64 12.2.0-14 [2437 kB]
2024-01-13T13:48:05.2674574Z #17 2.638 Get:47 http://deb.debian.org/debian bookworm/main amd64 gcc-12 amd64 12.2.0-14 [19.3 MB]
2024-01-13T13:48:05.2675595Z #17 2.718 Get:48 http://deb.debian.org/debian bookworm/main amd64 gcc amd64 4:12.2.0-3 [5216 B]
2024-01-13T13:48:05.4162895Z #17 2.718 Get:49 http://deb.debian.org/debian bookworm/main amd64 libc-dev-bin amd64 2.36-9+deb12u3 [45.2 kB]
2024-01-13T13:48:05.4165207Z #17 2.719 Get:50 http://deb.debian.org/debian-security bookworm-security/main amd64 linux-libc-dev amd64 6.1.69-1 [1910 kB]
2024-01-13T13:48:05.4167391Z #17 2.724 Get:51 http://deb.debian.org/debian bookworm/main amd64 libcrypt-dev amd64 1:4.4.33-2 [118 kB]
2024-01-13T13:48:05.4169612Z #17 2.724 Get:52 http://deb.debian.org/debian bookworm/main amd64 libtirpc-dev amd64 1.3.3+ds-1 [191 kB]
2024-01-13T13:48:05.4171520Z #17 2.725 Get:53 http://deb.debian.org/debian bookworm/main amd64 libnsl-dev amd64 1.3.0-2 [66.4 kB]
2024-01-13T13:48:05.4173623Z #17 2.726 Get:54 http://deb.debian.org/debian bookworm/main amd64 rpcsvc-proto amd64 1.4.3-1 [63.3 kB]
2024-01-13T13:48:05.4175620Z #17 2.726 Get:55 http://deb.debian.org/debian bookworm/main amd64 libc6-dev amd64 2.36-9+deb12u3 [1898 kB]
2024-01-13T13:48:05.4177967Z #17 2.735 Get:56 http://deb.debian.org/debian bookworm/main amd64 libstdc++-12-dev amd64 12.2.0-14 [2046 kB]
2024-01-13T13:48:05.4179976Z #17 2.743 Get:57 http://deb.debian.org/debian bookworm/main amd64 g++-12 amd64 12.2.0-14 [10.7 MB]
2024-01-13T13:48:05.4181667Z #17 2.787 Get:58 http://deb.debian.org/debian bookworm/main amd64 g++ amd64 4:12.2.0-3 [1356 B]
2024-01-13T13:48:05.4183558Z #17 2.787 Get:59 http://deb.debian.org/debian bookworm/main amd64 libnl-3-200 amd64 3.7.0-0.2+b1 [63.1 kB]
2024-01-13T13:48:05.4185707Z #17 2.788 Get:60 http://deb.debian.org/debian bookworm/main amd64 libnl-genl-3-200 amd64 3.7.0-0.2+b1 [21.6 kB]
2024-01-13T13:48:05.4187509Z #17 2.788 Get:61 http://deb.debian.org/debian bookworm/main amd64 htop amd64 3.2.2-2 [152 kB]
2024-01-13T13:48:05.4189282Z #17 2.789 Get:62 http://deb.debian.org/debian bookworm/main amd64 make amd64 4.3-4.1 [396 kB]
2024-01-13T13:48:05.5668206Z #17 2.882 debconf: delaying package configuration, since apt-utils is not installed
2024-01-13T13:48:05.5669632Z #17 2.901 Fetched 73.0 MB in 1s (102 MB/s)
2024-01-13T13:48:05.5670605Z #17 2.913 Selecting previously unselected package libssl3:amd64.
2024-01-13T13:48:05.5671629Z #17 2.913 (Reading database ... 
2024-01-13T13:48:05.5672283Z (Reading database ... 5%
2024-01-13T13:48:05.5672911Z (Reading database ... 10%
2024-01-13T13:48:05.5673612Z (Reading database ... 15%
2024-01-13T13:48:05.5674242Z (Reading database ... 20%
2024-01-13T13:48:05.5674845Z (Reading database ... 25%
2024-01-13T13:48:05.5675530Z (Reading database ... 30%
2024-01-13T13:48:05.5676173Z (Reading database ... 35%
2024-01-13T13:48:05.5676862Z (Reading database ... 40%
2024-01-13T13:48:05.5677515Z (Reading database ... 45%
2024-01-13T13:48:05.5678126Z (Reading database ... 50%
2024-01-13T13:48:05.5678824Z (Reading database ... 55%
2024-01-13T13:48:05.5679453Z (Reading database ... 60%
2024-01-13T13:48:05.5680061Z (Reading database ... 65%
2024-01-13T13:48:05.5680772Z (Reading database ... 70%
2024-01-13T13:48:05.5681383Z (Reading database ... 75%
2024-01-13T13:48:05.5682066Z (Reading database ... 80%
2024-01-13T13:48:05.5682687Z (Reading database ... 85%
2024-01-13T13:48:05.5683286Z (Reading database ... 90%
2024-01-13T13:48:05.5683992Z (Reading database ... 95%
2024-01-13T13:48:05.5684600Z (Reading database ... 100%
2024-01-13T13:48:05.5685454Z (Reading database ... 6098 files and directories currently installed.)
2024-01-13T13:48:05.5686858Z #17 2.918 Preparing to unpack .../libssl3_3.0.11-1~deb12u2_amd64.deb ...
2024-01-13T13:48:05.5687994Z #17 2.920 Unpacking libssl3:amd64 (3.0.11-1~deb12u2) ...
2024-01-13T13:48:05.6875149Z #17 3.040 Selecting previously unselected package libpython3.11-minimal:amd64.
2024-01-13T13:48:05.6876252Z #17 3.041 Preparing to unpack .../libpython3.11-minimal_3.11.2-6_amd64.deb ...
2024-01-13T13:48:05.6877022Z #17 3.042 Unpacking libpython3.11-minimal:amd64 (3.11.2-6) ...
2024-01-13T13:48:05.6877828Z #17 3.117 Selecting previously unselected package libexpat1:amd64.
2024-01-13T13:48:05.6878826Z #17 3.118 Preparing to unpack .../libexpat1_2.5.0-1_amd64.deb ...
2024-01-13T13:48:05.6879665Z #17 3.119 Unpacking libexpat1:amd64 (2.5.0-1) ...
2024-01-13T13:48:05.6880333Z #17 3.140 Selecting previously unselected package python3.11-minimal.
2024-01-13T13:48:05.8330429Z #17 3.141 Preparing to unpack .../python3.11-minimal_3.11.2-6_amd64.deb ...
2024-01-13T13:48:05.8331511Z #17 3.145 Unpacking python3.11-minimal (3.11.2-6) ...
2024-01-13T13:48:05.8332410Z #17 3.285 Setting up libssl3:amd64 (3.0.11-1~deb12u2) ...
2024-01-13T13:48:05.9835805Z #17 3.288 Setting up libpython3.11-minimal:amd64 (3.11.2-6) ...
2024-01-13T13:48:05.9837051Z #17 3.293 Setting up libexpat1:amd64 (2.5.0-1) ...
2024-01-13T13:48:05.9838092Z #17 3.296 Setting up python3.11-minimal (3.11.2-6) ...
2024-01-13T13:48:06.3908361Z #17 3.821 Selecting previously unselected package python3-minimal.
2024-01-13T13:48:06.3909332Z #17 3.821 (Reading database ... 
2024-01-13T13:48:06.3909966Z (Reading database ... 5%
2024-01-13T13:48:06.3910781Z (Reading database ... 10%
2024-01-13T13:48:06.3911443Z (Reading database ... 15%
2024-01-13T13:48:06.3912003Z (Reading database ... 20%
2024-01-13T13:48:06.3912379Z (Reading database ... 25%
2024-01-13T13:48:06.3912748Z (Reading database ... 30%
2024-01-13T13:48:06.3913218Z (Reading database ... 35%
2024-01-13T13:48:06.3913587Z (Reading database ... 40%
2024-01-13T13:48:06.3913961Z (Reading database ... 45%
2024-01-13T13:48:06.3914579Z (Reading database ... 50%
2024-01-13T13:48:06.3915252Z (Reading database ... 55%
2024-01-13T13:48:06.3916066Z (Reading database ... 60%
2024-01-13T13:48:06.3917162Z (Reading database ... 65%
2024-01-13T13:48:06.3917796Z (Reading database ... 70%
2024-01-13T13:48:06.3918284Z (Reading database ... 75%
2024-01-13T13:48:06.3918679Z (Reading database ... 80%
2024-01-13T13:48:06.3919183Z (Reading database ... 85%
2024-01-13T13:48:06.3919637Z (Reading database ... 90%
2024-01-13T13:48:06.3920194Z (Reading database ... 95%
2024-01-13T13:48:06.3920666Z (Reading database ... 100%
2024-01-13T13:48:06.3921228Z (Reading database ... 6426 files and directories currently installed.)
2024-01-13T13:48:06.3922217Z #17 3.826 Preparing to unpack .../00-python3-minimal_3.11.2-1+b1_amd64.deb ...
2024-01-13T13:48:06.3923192Z #17 3.827 Unpacking python3-minimal (3.11.2-1+b1) ...
2024-01-13T13:48:06.3924026Z #17 3.843 Selecting previously unselected package media-types.
2024-01-13T13:48:06.4932302Z #17 3.844 Preparing to unpack .../01-media-types_10.0.0_all.deb ...
2024-01-13T13:48:06.4933585Z #17 3.845 Unpacking media-types (10.0.0) ...
2024-01-13T13:48:06.4934775Z #17 3.862 Selecting previously unselected package libncursesw6:amd64.
2024-01-13T13:48:06.4935625Z #17 3.863 Preparing to unpack .../02-libncursesw6_6.4-4_amd64.deb ...
2024-01-13T13:48:06.4936491Z #17 3.864 Unpacking libncursesw6:amd64 (6.4-4) ...
2024-01-13T13:48:06.4937337Z #17 3.886 Selecting previously unselected package libkrb5support0:amd64.
2024-01-13T13:48:06.4939041Z #17 3.887 Preparing to unpack .../03-libkrb5support0_1.20.1-2+deb12u1_amd64.deb ...
2024-01-13T13:48:06.4940246Z #17 3.888 Unpacking libkrb5support0:amd64 (1.20.1-2+deb12u1) ...
2024-01-13T13:48:06.4941472Z #17 3.905 Selecting previously unselected package libk5crypto3:amd64.
2024-01-13T13:48:06.4942915Z #17 3.906 Preparing to unpack .../04-libk5crypto3_1.20.1-2+deb12u1_amd64.deb ...
2024-01-13T13:48:06.4944412Z #17 3.907 Unpacking libk5crypto3:amd64 (1.20.1-2+deb12u1) ...
2024-01-13T13:48:06.4945340Z #17 3.926 Selecting previously unselected package libkeyutils1:amd64.
2024-01-13T13:48:06.4946239Z #17 3.927 Preparing to unpack .../05-libkeyutils1_1.6.3-2_amd64.deb ...
2024-01-13T13:48:06.4946976Z #17 3.928 Unpacking libkeyutils1:amd64 (1.6.3-2) ...
2024-01-13T13:48:06.4947630Z #17 3.945 Selecting previously unselected package libkrb5-3:amd64.
2024-01-13T13:48:06.6089076Z #17 3.946 Preparing to unpack .../06-libkrb5-3_1.20.1-2+deb12u1_amd64.deb ...
2024-01-13T13:48:06.6090226Z #17 3.947 Unpacking libkrb5-3:amd64 (1.20.1-2+deb12u1) ...
2024-01-13T13:48:06.6091136Z #17 3.983 Selecting previously unselected package libgssapi-krb5-2:amd64.
2024-01-13T13:48:06.6092275Z #17 3.984 Preparing to unpack .../07-libgssapi-krb5-2_1.20.1-2+deb12u1_amd64.deb ...
2024-01-13T13:48:06.6093196Z #17 3.985 Unpacking libgssapi-krb5-2:amd64 (1.20.1-2+deb12u1) ...
2024-01-13T13:48:06.6095254Z #17 4.006 Selecting previously unselected package libtirpc-common.
2024-01-13T13:48:06.6096510Z #17 4.007 Preparing to unpack .../08-libtirpc-common_1.3.3+ds-1_all.deb ...
2024-01-13T13:48:06.6097280Z #17 4.007 Unpacking libtirpc-common (1.3.3+ds-1) ...
2024-01-13T13:48:06.6098625Z #17 4.022 Selecting previously unselected package libtirpc3:amd64.
2024-01-13T13:48:06.6099401Z #17 4.023 Preparing to unpack .../09-libtirpc3_1.3.3+ds-1_amd64.deb ...
2024-01-13T13:48:06.6100257Z #17 4.024 Unpacking libtirpc3:amd64 (1.3.3+ds-1) ...
2024-01-13T13:48:06.6100859Z #17 4.043 Selecting previously unselected package libnsl2:amd64.
2024-01-13T13:48:06.6101576Z #17 4.044 Preparing to unpack .../10-libnsl2_1.3.0-2_amd64.deb ...
2024-01-13T13:48:06.6102268Z #17 4.045 Unpacking libnsl2:amd64 (1.3.0-2) ...
2024-01-13T13:48:06.6102909Z #17 4.061 Selecting previously unselected package readline-common.
2024-01-13T13:48:06.7113632Z #17 4.062 Preparing to unpack .../11-readline-common_8.2-1.3_all.deb ...
2024-01-13T13:48:06.7114399Z #17 4.064 Unpacking readline-common (8.2-1.3) ...
2024-01-13T13:48:06.7115188Z #17 4.082 Selecting previously unselected package libreadline8:amd64.
2024-01-13T13:48:06.7115992Z #17 4.083 Preparing to unpack .../12-libreadline8_8.2-1.3_amd64.deb ...
2024-01-13T13:48:06.7116987Z #17 4.084 Unpacking libreadline8:amd64 (8.2-1.3) ...
2024-01-13T13:48:06.7117689Z #17 4.108 Selecting previously unselected package libsqlite3-0:amd64.
2024-01-13T13:48:06.7118434Z #17 4.109 Preparing to unpack .../13-libsqlite3-0_3.40.1-2_amd64.deb ...
2024-01-13T13:48:06.7119181Z #17 4.110 Unpacking libsqlite3-0:amd64 (3.40.1-2) ...
2024-01-13T13:48:06.7120143Z #17 4.164 Selecting previously unselected package libpython3.11-stdlib:amd64.
2024-01-13T13:48:06.8397500Z #17 4.165 Preparing to unpack .../14-libpython3.11-stdlib_3.11.2-6_amd64.deb ...
2024-01-13T13:48:06.8398530Z #17 4.166 Unpacking libpython3.11-stdlib:amd64 (3.11.2-6) ...
2024-01-13T13:48:06.8399175Z #17 4.292 Selecting previously unselected package python3.11.
2024-01-13T13:48:06.9905507Z #17 4.294 Preparing to unpack .../15-python3.11_3.11.2-6_amd64.deb ...
2024-01-13T13:48:06.9906270Z #17 4.295 Unpacking python3.11 (3.11.2-6) ...
2024-01-13T13:48:06.9907133Z #17 4.317 Selecting previously unselected package libpython3-stdlib:amd64.
2024-01-13T13:48:06.9908218Z #17 4.318 Preparing to unpack .../16-libpython3-stdlib_3.11.2-1+b1_amd64.deb ...
2024-01-13T13:48:06.9909086Z #17 4.319 Unpacking libpython3-stdlib:amd64 (3.11.2-1+b1) ...
2024-01-13T13:48:06.9910221Z #17 4.336 Setting up python3-minimal (3.11.2-1+b1) ...
2024-01-13T13:48:07.1411981Z #17 4.446 Selecting previously unselected package python3.
2024-01-13T13:48:07.1412845Z #17 4.446 (Reading database ... 
2024-01-13T13:48:07.1413322Z (Reading database ... 5%
2024-01-13T13:48:07.1413741Z (Reading database ... 10%
2024-01-13T13:48:07.1414226Z (Reading database ... 15%
2024-01-13T13:48:07.1414644Z (Reading database ... 20%
2024-01-13T13:48:07.1415033Z (Reading database ... 25%
2024-01-13T13:48:07.1415485Z (Reading database ... 30%
2024-01-13T13:48:07.1415884Z (Reading database ... 35%
2024-01-13T13:48:07.1416333Z (Reading database ... 40%
2024-01-13T13:48:07.1416733Z (Reading database ... 45%
2024-01-13T13:48:07.1417111Z (Reading database ... 50%
2024-01-13T13:48:07.1417808Z (Reading database ... 55%
2024-01-13T13:48:07.1418369Z (Reading database ... 60%
2024-01-13T13:48:07.1418958Z (Reading database ... 65%
2024-01-13T13:48:07.1419592Z (Reading database ... 70%
2024-01-13T13:48:07.1419996Z (Reading database ... 75%
2024-01-13T13:48:07.1420462Z (Reading database ... 80%
2024-01-13T13:48:07.1420864Z (Reading database ... 85%
2024-01-13T13:48:07.1421261Z (Reading database ... 90%
2024-01-13T13:48:07.1421719Z (Reading database ... 95%
2024-01-13T13:48:07.1422471Z (Reading database ... 100%
2024-01-13T13:48:07.1423041Z (Reading database ... 6934 files and directories currently installed.)
2024-01-13T13:48:07.1424106Z #17 4.452 Preparing to unpack .../00-python3_3.11.2-1+b1_amd64.deb ...
2024-01-13T13:48:07.1424792Z #17 4.456 Unpacking python3 (3.11.2-1+b1) ...
2024-01-13T13:48:07.1425603Z #17 4.473 Selecting previously unselected package binutils-common:amd64.
2024-01-13T13:48:07.1426398Z #17 4.473 Preparing to unpack .../01-binutils-common_2.40-2_amd64.deb ...
2024-01-13T13:48:07.1427094Z #17 4.475 Unpacking binutils-common:amd64 (2.40-2) ...
2024-01-13T13:48:07.2636689Z #17 4.638 Selecting previously unselected package libbinutils:amd64.
2024-01-13T13:48:07.2638370Z #17 4.639 Preparing to unpack .../02-libbinutils_2.40-2_amd64.deb ...
2024-01-13T13:48:07.2639197Z #17 4.640 Unpacking libbinutils:amd64 (2.40-2) ...
2024-01-13T13:48:07.2639907Z #17 4.690 Selecting previously unselected package libctf-nobfd0:amd64.
2024-01-13T13:48:07.2640775Z #17 4.692 Preparing to unpack .../03-libctf-nobfd0_2.40-2_amd64.deb ...
2024-01-13T13:48:07.2641477Z #17 4.693 Unpacking libctf-nobfd0:amd64 (2.40-2) ...
2024-01-13T13:48:07.2642065Z #17 4.716 Selecting previously unselected package libctf0:amd64.
2024-01-13T13:48:07.3680061Z #17 4.717 Preparing to unpack .../04-libctf0_2.40-2_amd64.deb ...
2024-01-13T13:48:07.3680894Z #17 4.718 Unpacking libctf0:amd64 (2.40-2) ...
2024-01-13T13:48:07.3681826Z #17 4.738 Selecting previously unselected package libgprofng0:amd64.
2024-01-13T13:48:07.3682974Z #17 4.739 Preparing to unpack .../05-libgprofng0_2.40-2_amd64.deb ...
2024-01-13T13:48:07.3683904Z #17 4.740 Unpacking libgprofng0:amd64 (2.40-2) ...
2024-01-13T13:48:07.3684636Z #17 4.804 Selecting previously unselected package libjansson4:amd64.
2024-01-13T13:48:07.3685498Z #17 4.805 Preparing to unpack .../06-libjansson4_2.14-2_amd64.deb ...
2024-01-13T13:48:07.3688253Z #17 4.806 Unpacking libjansson4:amd64 (2.14-2) ...
2024-01-13T13:48:07.3689206Z #17 4.821 Selecting previously unselected package binutils-x86-64-linux-gnu.
2024-01-13T13:48:07.5190990Z #17 4.822 Preparing to unpack .../07-binutils-x86-64-linux-gnu_2.40-2_amd64.deb ...
2024-01-13T13:48:07.5191849Z #17 4.822 Unpacking binutils-x86-64-linux-gnu (2.40-2) ...
2024-01-13T13:48:07.6220959Z #17 4.990 Selecting previously unselected package binutils.
2024-01-13T13:48:07.6222357Z #17 4.991 Preparing to unpack .../08-binutils_2.40-2_amd64.deb ...
2024-01-13T13:48:07.6223003Z #17 4.992 Unpacking binutils (2.40-2) ...
2024-01-13T13:48:07.6223715Z #17 5.014 Selecting previously unselected package libisl23:amd64.
2024-01-13T13:48:07.6224449Z #17 5.015 Preparing to unpack .../09-libisl23_0.25-1_amd64.deb ...
2024-01-13T13:48:07.6225094Z #17 5.016 Unpacking libisl23:amd64 (0.25-1) ...
2024-01-13T13:48:07.6225750Z #17 5.075 Selecting previously unselected package libmpfr6:amd64.
2024-01-13T13:48:07.7733168Z #17 5.076 Preparing to unpack .../10-libmpfr6_4.2.0-1_amd64.deb ...
2024-01-13T13:48:07.7734324Z #17 5.077 Unpacking libmpfr6:amd64 (4.2.0-1) ...
2024-01-13T13:48:07.7735333Z #17 5.114 Selecting previously unselected package libmpc3:amd64.
2024-01-13T13:48:07.7736685Z #17 5.115 Preparing to unpack .../11-libmpc3_1.3.1-1_amd64.deb ...
2024-01-13T13:48:07.7737974Z #17 5.117 Unpacking libmpc3:amd64 (1.3.1-1) ...
2024-01-13T13:48:07.7739018Z #17 5.133 Selecting previously unselected package cpp-12.
2024-01-13T13:48:07.7740281Z #17 5.134 Preparing to unpack .../12-cpp-12_12.2.0-14_amd64.deb ...
2024-01-13T13:48:07.7741295Z #17 5.135 Unpacking cpp-12 (12.2.0-14) ...
2024-01-13T13:48:08.1874672Z #17 5.624 Selecting previously unselected package cpp.
2024-01-13T13:48:08.1876055Z #17 5.625 Preparing to unpack .../13-cpp_4%3a12.2.0-3_amd64.deb ...
2024-01-13T13:48:08.1877277Z #17 5.626 Unpacking cpp (4:12.2.0-3) ...
2024-01-13T13:48:08.1878128Z #17 5.640 Selecting previously unselected package dumb-init.
2024-01-13T13:48:08.3383534Z #17 5.641 Preparing to unpack .../14-dumb-init_1.2.5-2_amd64.deb ...
2024-01-13T13:48:08.3384960Z #17 5.642 Unpacking dumb-init (1.2.5-2) ...
2024-01-13T13:48:08.3386126Z #17 5.657 Selecting previously unselected package libcc1-0:amd64.
2024-01-13T13:48:08.3387354Z #17 5.658 Preparing to unpack .../15-libcc1-0_12.2.0-14_amd64.deb ...
2024-01-13T13:48:08.3388404Z #17 5.659 Unpacking libcc1-0:amd64 (12.2.0-14) ...
2024-01-13T13:48:08.3389478Z #17 5.676 Selecting previously unselected package libgomp1:amd64.
2024-01-13T13:48:08.3390415Z #17 5.677 Preparing to unpack .../16-libgomp1_12.2.0-14_amd64.deb ...
2024-01-13T13:48:08.3391529Z #17 5.678 Unpacking libgomp1:amd64 (12.2.0-14) ...
2024-01-13T13:48:08.3392264Z #17 5.699 Selecting previously unselected package libitm1:amd64.
2024-01-13T13:48:08.3392987Z #17 5.700 Preparing to unpack .../17-libitm1_12.2.0-14_amd64.deb ...
2024-01-13T13:48:08.3393712Z #17 5.701 Unpacking libitm1:amd64 (12.2.0-14) ...
2024-01-13T13:48:08.3394362Z #17 5.717 Selecting previously unselected package libatomic1:amd64.
2024-01-13T13:48:08.3395119Z #17 5.718 Preparing to unpack .../18-libatomic1_12.2.0-14_amd64.deb ...
2024-01-13T13:48:08.3395892Z #17 5.719 Unpacking libatomic1:amd64 (12.2.0-14) ...
2024-01-13T13:48:08.3396493Z #17 5.735 Selecting previously unselected package libasan8:amd64.
2024-01-13T13:48:08.3397338Z #17 5.736 Preparing to unpack .../19-libasan8_12.2.0-14_amd64.deb ...
2024-01-13T13:48:08.3397982Z #17 5.737 Unpacking libasan8:amd64 (12.2.0-14) ...
2024-01-13T13:48:08.4886810Z #17 5.886 Selecting previously unselected package liblsan0:amd64.
2024-01-13T13:48:08.4888455Z #17 5.887 Preparing to unpack .../20-liblsan0_12.2.0-14_amd64.deb ...
2024-01-13T13:48:08.4889472Z #17 5.888 Unpacking liblsan0:amd64 (12.2.0-14) ...
2024-01-13T13:48:08.6397042Z #17 5.962 Selecting previously unselected package libtsan2:amd64.
2024-01-13T13:48:08.6398544Z #17 5.963 Preparing to unpack .../21-libtsan2_12.2.0-14_amd64.deb ...
2024-01-13T13:48:08.6399891Z #17 5.964 Unpacking libtsan2:amd64 (12.2.0-14) ...
2024-01-13T13:48:08.7525679Z #17 6.109 Selecting previously unselected package libubsan1:amd64.
2024-01-13T13:48:08.7527387Z #17 6.111 Preparing to unpack .../22-libubsan1_12.2.0-14_amd64.deb ...
2024-01-13T13:48:08.7528777Z #17 6.112 Unpacking libubsan1:amd64 (12.2.0-14) ...
2024-01-13T13:48:08.7529993Z #17 6.183 Selecting previously unselected package libquadmath0:amd64.
2024-01-13T13:48:08.7531401Z #17 6.184 Preparing to unpack .../23-libquadmath0_12.2.0-14_amd64.deb ...
2024-01-13T13:48:08.7532169Z #17 6.185 Unpacking libquadmath0:amd64 (12.2.0-14) ...
2024-01-13T13:48:08.7533319Z #17 6.205 Selecting previously unselected package libgcc-12-dev:amd64.
2024-01-13T13:48:08.9028883Z #17 6.206 Preparing to unpack .../24-libgcc-12-dev_12.2.0-14_amd64.deb ...
2024-01-13T13:48:08.9029782Z #17 6.207 Unpacking libgcc-12-dev:amd64 (12.2.0-14) ...
2024-01-13T13:48:09.0542645Z #17 6.366 Selecting previously unselected package gcc-12.
2024-01-13T13:48:09.0543916Z #17 6.367 Preparing to unpack .../25-gcc-12_12.2.0-14_amd64.deb ...
2024-01-13T13:48:09.0545231Z #17 6.368 Unpacking gcc-12 (12.2.0-14) ...
2024-01-13T13:48:09.6550111Z #17 6.978 Selecting previously unselected package gcc.
2024-01-13T13:48:09.6551848Z #17 6.979 Preparing to unpack .../26-gcc_4%3a12.2.0-3_amd64.deb ...
2024-01-13T13:48:09.6552954Z #17 6.980 Unpacking gcc (4:12.2.0-3) ...
2024-01-13T13:48:09.6554178Z #17 6.997 Selecting previously unselected package libc-dev-bin.
2024-01-13T13:48:09.6555672Z #17 6.998 Preparing to unpack .../27-libc-dev-bin_2.36-9+deb12u3_amd64.deb ...
2024-01-13T13:48:09.6556964Z #17 6.999 Unpacking libc-dev-bin (2.36-9+deb12u3) ...
2024-01-13T13:48:09.6558391Z #17 7.015 Selecting previously unselected package linux-libc-dev:amd64.
2024-01-13T13:48:09.6559823Z #17 7.016 Preparing to unpack .../28-linux-libc-dev_6.1.69-1_amd64.deb ...
2024-01-13T13:48:09.6561221Z #17 7.017 Unpacking linux-libc-dev:amd64 (6.1.69-1) ...
2024-01-13T13:48:09.7566805Z #17 7.203 Selecting previously unselected package libcrypt-dev:amd64.
2024-01-13T13:48:09.7568139Z #17 7.204 Preparing to unpack .../29-libcrypt-dev_1%3a4.4.33-2_amd64.deb ...
2024-01-13T13:48:09.7569192Z #17 7.209 Unpacking libcrypt-dev:amd64 (1:4.4.33-2) ...
2024-01-13T13:48:09.9077817Z #17 7.230 Selecting previously unselected package libtirpc-dev:amd64.
2024-01-13T13:48:09.9079599Z #17 7.231 Preparing to unpack .../30-libtirpc-dev_1.3.3+ds-1_amd64.deb ...
2024-01-13T13:48:09.9080876Z #17 7.232 Unpacking libtirpc-dev:amd64 (1.3.3+ds-1) ...
2024-01-13T13:48:09.9082411Z #17 7.260 Selecting previously unselected package libnsl-dev:amd64.
2024-01-13T13:48:09.9083782Z #17 7.261 Preparing to unpack .../31-libnsl-dev_1.3.0-2_amd64.deb ...
2024-01-13T13:48:09.9084968Z #17 7.263 Unpacking libnsl-dev:amd64 (1.3.0-2) ...
2024-01-13T13:48:09.9086295Z #17 7.280 Selecting previously unselected package rpcsvc-proto.
2024-01-13T13:48:09.9087636Z #17 7.281 Preparing to unpack .../32-rpcsvc-proto_1.4.3-1_amd64.deb ...
2024-01-13T13:48:09.9088819Z #17 7.282 Unpacking rpcsvc-proto (1.4.3-1) ...
2024-01-13T13:48:09.9090108Z #17 7.303 Selecting previously unselected package libc6-dev:amd64.
2024-01-13T13:48:09.9091494Z #17 7.304 Preparing to unpack .../33-libc6-dev_2.36-9+deb12u3_amd64.deb ...
2024-01-13T13:48:09.9092934Z #17 7.305 Unpacking libc6-dev:amd64 (2.36-9+deb12u3) ...
2024-01-13T13:48:10.0586978Z #17 7.453 Selecting previously unselected package libstdc++-12-dev:amd64.
2024-01-13T13:48:10.0590109Z #17 7.454 Preparing to unpack .../34-libstdc++-12-dev_12.2.0-14_amd64.deb ...
2024-01-13T13:48:10.0591315Z #17 7.455 Unpacking libstdc++-12-dev:amd64 (12.2.0-14) ...
2024-01-13T13:48:10.3595508Z #17 7.670 Selecting previously unselected package g++-12.
2024-01-13T13:48:10.3597143Z #17 7.672 Preparing to unpack .../35-g++-12_12.2.0-14_amd64.deb ...
2024-01-13T13:48:10.3598460Z #17 7.673 Unpacking g++-12 (12.2.0-14) ...
2024-01-13T13:48:10.7659643Z #17 8.180 Selecting previously unselected package g++.
2024-01-13T13:48:10.7660795Z #17 8.182 Preparing to unpack .../36-g++_4%3a12.2.0-3_amd64.deb ...
2024-01-13T13:48:10.7661468Z #17 8.183 Unpacking g++ (4:12.2.0-3) ...
2024-01-13T13:48:10.7662132Z #17 8.198 Selecting previously unselected package libnl-3-200:amd64.
2024-01-13T13:48:10.7662996Z #17 8.199 Preparing to unpack .../37-libnl-3-200_3.7.0-0.2+b1_amd64.deb ...
2024-01-13T13:48:10.7663709Z #17 8.200 Unpacking libnl-3-200:amd64 (3.7.0-0.2+b1) ...
2024-01-13T13:48:10.7664413Z #17 8.219 Selecting previously unselected package libnl-genl-3-200:amd64.
2024-01-13T13:48:10.8686596Z #17 8.220 Preparing to unpack .../38-libnl-genl-3-200_3.7.0-0.2+b1_amd64.deb ...
2024-01-13T13:48:10.8687478Z #17 8.221 Unpacking libnl-genl-3-200:amd64 (3.7.0-0.2+b1) ...
2024-01-13T13:48:10.8688288Z #17 8.235 Selecting previously unselected package htop.
2024-01-13T13:48:10.8689191Z #17 8.236 Preparing to unpack .../39-htop_3.2.2-2_amd64.deb ...
2024-01-13T13:48:10.8689925Z #17 8.237 Unpacking htop (3.2.2-2) ...
2024-01-13T13:48:10.8690726Z #17 8.261 Selecting previously unselected package make.
2024-01-13T13:48:10.8691491Z #17 8.262 Preparing to unpack .../40-make_4.3-4.1_amd64.deb ...
2024-01-13T13:48:10.8692355Z #17 8.263 Unpacking make (4.3-4.1) ...
2024-01-13T13:48:10.8692889Z #17 8.307 Setting up media-types (10.0.0) ...
2024-01-13T13:48:10.8693430Z #17 8.311 Setting up dumb-init (1.2.5-2) ...
2024-01-13T13:48:10.8694222Z #17 8.314 Setting up libkeyutils1:amd64 (1.6.3-2) ...
2024-01-13T13:48:10.8694831Z #17 8.317 Setting up libtirpc-common (1.3.3+ds-1) ...
2024-01-13T13:48:10.8695445Z #17 8.321 Setting up libsqlite3-0:amd64 (3.40.1-2) ...
2024-01-13T13:48:10.9712636Z #17 8.324 Setting up binutils-common:amd64 (2.40-2) ...
2024-01-13T13:48:10.9713701Z #17 8.329 Setting up linux-libc-dev:amd64 (6.1.69-1) ...
2024-01-13T13:48:10.9714629Z #17 8.331 Setting up libctf-nobfd0:amd64 (2.40-2) ...
2024-01-13T13:48:10.9715378Z #17 8.334 Setting up libgomp1:amd64 (12.2.0-14) ...
2024-01-13T13:48:10.9716159Z #17 8.337 Setting up libjansson4:amd64 (2.14-2) ...
2024-01-13T13:48:10.9716950Z #17 8.340 Setting up libkrb5support0:amd64 (1.20.1-2+deb12u1) ...
2024-01-13T13:48:10.9717752Z #17 8.342 Setting up rpcsvc-proto (1.4.3-1) ...
2024-01-13T13:48:10.9718788Z #17 8.345 Setting up make (4.3-4.1) ...
2024-01-13T13:48:10.9719394Z #17 8.347 Setting up libmpfr6:amd64 (4.2.0-1) ...
2024-01-13T13:48:10.9720067Z #17 8.350 Setting up libquadmath0:amd64 (12.2.0-14) ...
2024-01-13T13:48:10.9720939Z #17 8.353 Setting up libmpc3:amd64 (1.3.1-1) ...
2024-01-13T13:48:10.9721560Z #17 8.356 Setting up libatomic1:amd64 (12.2.0-14) ...
2024-01-13T13:48:10.9722306Z #17 8.359 Setting up libncursesw6:amd64 (6.4-4) ...
2024-01-13T13:48:10.9723039Z #17 8.362 Setting up libk5crypto3:amd64 (1.20.1-2+deb12u1) ...
2024-01-13T13:48:10.9723706Z #17 8.365 Setting up libubsan1:amd64 (12.2.0-14) ...
2024-01-13T13:48:10.9724404Z #17 8.368 Setting up libcrypt-dev:amd64 (1:4.4.33-2) ...
2024-01-13T13:48:10.9724998Z #17 8.374 Setting up libasan8:amd64 (12.2.0-14) ...
2024-01-13T13:48:10.9725688Z #17 8.377 Setting up libnl-3-200:amd64 (3.7.0-0.2+b1) ...
2024-01-13T13:48:10.9726532Z #17 8.381 Setting up libkrb5-3:amd64 (1.20.1-2+deb12u1) ...
2024-01-13T13:48:10.9727134Z #17 8.384 Setting up libtsan2:amd64 (12.2.0-14) ...
2024-01-13T13:48:10.9727800Z #17 8.387 Setting up libbinutils:amd64 (2.40-2) ...
2024-01-13T13:48:10.9728394Z #17 8.390 Setting up libisl23:amd64 (0.25-1) ...
2024-01-13T13:48:10.9728955Z #17 8.392 Setting up libc-dev-bin (2.36-9+deb12u3) ...
2024-01-13T13:48:10.9729652Z #17 8.399 Setting up readline-common (8.2-1.3) ...
2024-01-13T13:48:10.9730251Z #17 8.403 Setting up libcc1-0:amd64 (12.2.0-14) ...
2024-01-13T13:48:10.9730864Z #17 8.406 Setting up liblsan0:amd64 (12.2.0-14) ...
2024-01-13T13:48:10.9731681Z #17 8.409 Setting up libitm1:amd64 (12.2.0-14) ...
2024-01-13T13:48:10.9732271Z #17 8.412 Setting up libctf0:amd64 (2.40-2) ...
2024-01-13T13:48:10.9732865Z #17 8.415 Setting up cpp-12 (12.2.0-14) ...
2024-01-13T13:48:10.9733628Z #17 8.418 Setting up libreadline8:amd64 (8.2-1.3) ...
2024-01-13T13:48:10.9734277Z #17 8.421 Setting up libgprofng0:amd64 (2.40-2) ...
2024-01-13T13:48:10.9734975Z #17 8.424 Setting up libgcc-12-dev:amd64 (12.2.0-14) ...
2024-01-13T13:48:11.1217815Z #17 8.427 Setting up libgssapi-krb5-2:amd64 (1.20.1-2+deb12u1) ...
2024-01-13T13:48:11.1219065Z #17 8.432 Setting up cpp (4:12.2.0-3) ...
2024-01-13T13:48:11.1220336Z #17 8.438 Setting up libnl-genl-3-200:amd64 (3.7.0-0.2+b1) ...
2024-01-13T13:48:11.1221508Z #17 8.441 Setting up binutils-x86-64-linux-gnu (2.40-2) ...
2024-01-13T13:48:11.1222634Z #17 8.444 Setting up libtirpc3:amd64 (1.3.3+ds-1) ...
2024-01-13T13:48:11.1223783Z #17 8.447 Setting up htop (3.2.2-2) ...
2024-01-13T13:48:11.1224661Z #17 8.449 Setting up binutils (2.40-2) ...
2024-01-13T13:48:11.1225731Z #17 8.452 Setting up libtirpc-dev:amd64 (1.3.3+ds-1) ...
2024-01-13T13:48:11.1226897Z #17 8.455 Setting up gcc-12 (12.2.0-14) ...
2024-01-13T13:48:11.1227879Z #17 8.459 Setting up libnsl2:amd64 (1.3.0-2) ...
2024-01-13T13:48:11.1229161Z #17 8.461 Setting up libpython3.11-stdlib:amd64 (3.11.2-6) ...
2024-01-13T13:48:11.1230204Z #17 8.464 Setting up gcc (4:12.2.0-3) ...
2024-01-13T13:48:11.1231195Z #17 8.473 Setting up libnsl-dev:amd64 (1.3.0-2) ...
2024-01-13T13:48:11.1232485Z #17 8.476 Setting up libc6-dev:amd64 (2.36-9+deb12u3) ...
2024-01-13T13:48:11.1233700Z #17 8.479 Setting up libpython3-stdlib:amd64 (3.11.2-1+b1) ...
2024-01-13T13:48:11.1234899Z #17 8.482 Setting up python3.11 (3.11.2-6) ...
2024-01-13T13:48:11.6756764Z #17 9.044 Setting up libstdc++-12-dev:amd64 (12.2.0-14) ...
2024-01-13T13:48:11.6757725Z #17 9.047 Setting up python3 (3.11.2-1+b1) ...
2024-01-13T13:48:11.6758725Z #17 9.121 Setting up g++-12 (12.2.0-14) ...
2024-01-13T13:48:11.6759304Z #17 9.124 Setting up g++ (4:12.2.0-3) ...
2024-01-13T13:48:11.6760472Z #17 9.128 update-alternatives: using /usr/bin/g++ to provide /usr/bin/c++ (c++) in auto mode
2024-01-13T13:48:11.8259004Z #17 9.131 Processing triggers for libc-bin (2.36-9+deb12u3) ...
2024-01-13T13:48:12.5772961Z #17 DONE 9.9s
2024-01-13T13:48:12.5773349Z 
2024-01-13T13:48:12.5773962Z #18 [stage-0  8/12] COPY package-lock.json .
2024-01-13T13:48:12.5774904Z #18 DONE 0.0s
2024-01-13T13:48:12.5775184Z 
2024-01-13T13:48:12.5776101Z #19 [stage-0  9/12] COPY package.json .
2024-01-13T13:48:12.5776946Z #19 DONE 0.0s
2024-01-13T13:48:12.5777229Z 
2024-01-13T13:48:12.5778147Z #20 [stage-0 10/12] RUN --mount=type=cache,target=/root/.cache npm ci
2024-01-13T13:48:13.4295120Z #20 0.941 npm WARN EBADENGINE Unsupported engine {
2024-01-13T13:48:13.4296588Z #20 0.941 npm WARN EBADENGINE   package: 'hawk@0.10.2',
2024-01-13T13:48:13.4298230Z #20 0.941 npm WARN EBADENGINE   required: { node: '0.8.x' },
2024-01-13T13:48:13.5797783Z #20 0.941 npm WARN EBADENGINE   current: { node: 'v20.10.0', npm: '10.2.3' }
2024-01-13T13:48:13.5798643Z #20 0.942 npm WARN EBADENGINE }
2024-01-13T13:48:13.5799179Z #20 0.942 npm WARN EBADENGINE Unsupported engine {
2024-01-13T13:48:13.5799822Z #20 0.942 npm WARN EBADENGINE   package: 'hoek@0.7.6',
2024-01-13T13:48:13.5800574Z #20 0.942 npm WARN EBADENGINE   required: { node: '0.8.x' },
2024-01-13T13:48:13.5801292Z #20 0.942 npm WARN EBADENGINE   current: { node: 'v20.10.0', npm: '10.2.3' }
2024-01-13T13:48:13.5801886Z #20 0.942 npm WARN EBADENGINE }
2024-01-13T13:48:18.9483328Z #20 6.330 npm WARN deprecated sntp@0.2.4: This module moved to @hapi/sntp. Please make sure to switch over as this distribution is no longer supported and may contain bugs and critical security issues.
2024-01-13T13:48:18.9488184Z #20 6.410 npm WARN deprecated cryptiles@0.1.0: This version has been deprecated in accordance with the hapi support policy (hapi.im/support). Please upgrade to the latest version to get the best features, bug fixes, and security patches. If you are unable to upgrade at this time, paid support is available for older versions (hapi.im/commercial).
2024-01-13T13:48:19.0993624Z #20 6.460 npm WARN deprecated cryptiles@0.2.2: This version has been deprecated in accordance with the hapi support policy (hapi.im/support). Please upgrade to the latest version to get the best features, bug fixes, and security patches. If you are unable to upgrade at this time, paid support is available for older versions (hapi.im/commercial).
2024-01-13T13:48:19.0998327Z #20 6.516 npm WARN deprecated boom@0.3.1: This version has been deprecated in accordance with the hapi support policy (hapi.im/support). Please upgrade to the latest version to get the best features, bug fixes, and security patches. If you are unable to upgrade at this time, paid support is available for older versions (hapi.im/commercial).
2024-01-13T13:48:19.1000734Z #20 6.549 npm WARN deprecated sntp@0.1.2: This module moved to @hapi/sntp. Please make sure to switch over as this distribution is no longer supported and may contain bugs and critical security issues.
2024-01-13T13:48:19.4005786Z #20 6.779 npm WARN deprecated hoek@0.9.1: This version has been deprecated in accordance with the hapi support policy (hapi.im/support). Please upgrade to the latest version to get the best features, bug fixes, and security patches. If you are unable to upgrade at this time, paid support is available for older versions (hapi.im/commercial).
2024-01-13T13:48:19.4009478Z #20 6.786 npm WARN deprecated hoek@0.4.2: This version has been deprecated in accordance with the hapi support policy (hapi.im/support). Please upgrade to the latest version to get the best features, bug fixes, and security patches. If you are unable to upgrade at this time, paid support is available for older versions (hapi.im/commercial).
2024-01-13T13:48:19.4014515Z #20 6.801 npm WARN deprecated hoek@0.4.2: This version has been deprecated in accordance with the hapi support policy (hapi.im/support). Please upgrade to the latest version to get the best features, bug fixes, and security patches. If you are unable to upgrade at this time, paid support is available for older versions (hapi.im/commercial).
2024-01-13T13:48:19.4019757Z #20 6.818 npm WARN deprecated boom@0.4.2: This version has been deprecated in accordance with the hapi support policy (hapi.im/support). Please upgrade to the latest version to get the best features, bug fixes, and security patches. If you are unable to upgrade at this time, paid support is available for older versions (hapi.im/commercial).
2024-01-13T13:48:19.4025491Z #20 6.821 npm WARN deprecated hoek@0.7.6: This version has been deprecated in accordance with the hapi support policy (hapi.im/support). Please upgrade to the latest version to get the best features, bug fixes, and security patches. If you are unable to upgrade at this time, paid support is available for older versions (hapi.im/commercial).
2024-01-13T13:48:19.6851828Z #20 7.046 npm WARN deprecated node-uuid@1.4.8: Use uuid module instead
2024-01-13T13:48:19.6854840Z #20 7.139 npm WARN deprecated hawk@0.10.2: This module moved to @hapi/hawk. Please make sure to switch over as this distribution is no longer supported and may contain bugs and critical security issues.
2024-01-13T13:48:19.9859463Z #20 7.388 npm WARN deprecated hawk@1.0.0: This module moved to @hapi/hawk. Please make sure to switch over as this distribution is no longer supported and may contain bugs and critical security issues.
2024-01-13T13:48:20.2863789Z #20 7.656 npm WARN deprecated request@2.16.6: request has been deprecated, see https://github.com/request/request/issues/3142
2024-01-13T13:48:20.4371641Z #20 7.803 npm WARN deprecated request@2.27.0: request has been deprecated, see https://github.com/request/request/issues/3142
2024-01-13T13:48:24.9458522Z #20 12.39 
2024-01-13T13:48:24.9459789Z #20 12.39 added 1044 packages, and audited 1045 packages in 12s
2024-01-13T13:48:24.9461150Z #20 12.39 
2024-01-13T13:48:24.9462139Z #20 12.39 168 packages are looking for funding
2024-01-13T13:48:24.9463964Z #20 12.39   run `npm fund` for details
2024-01-13T13:48:24.9465053Z #20 12.40 
2024-01-13T13:48:24.9465955Z #20 12.40 17 vulnerabilities (1 moderate, 11 high, 5 critical)
2024-01-13T13:48:24.9467136Z #20 12.40 
2024-01-13T13:48:24.9468000Z #20 12.40 To address issues that do not require attention, run:
2024-01-13T13:48:24.9469010Z #20 12.40   npm audit fix
2024-01-13T13:48:24.9469672Z #20 12.40 
2024-01-13T13:48:24.9470370Z #20 12.40 To address all issues (including breaking changes), run:
2024-01-13T13:48:24.9471577Z #20 12.40   npm audit fix --force
2024-01-13T13:48:24.9472293Z #20 12.40 
2024-01-13T13:48:24.9472809Z #20 12.40 Run `npm audit` for details.
2024-01-13T13:48:24.9473609Z #20 12.40 npm notice 
2024-01-13T13:48:24.9474483Z #20 12.40 npm notice New minor version of npm available! 10.2.3 -> 10.3.0
2024-01-13T13:48:24.9475283Z #20 12.40 npm notice Changelog: <https://github.com/npm/cli/releases/tag/v10.3.0>
2024-01-13T13:48:24.9476132Z #20 12.40 npm notice Run `npm install -g npm@10.3.0` to update!
2024-01-13T13:48:24.9476652Z #20 12.40 npm notice 
2024-01-13T13:48:25.8481142Z #20 DONE 13.3s
2024-01-13T13:48:25.8481594Z 
2024-01-13T13:48:25.8482195Z #21 [stage-0 11/12] COPY . .
2024-01-13T13:48:25.9983087Z #21 DONE 0.1s
2024-01-13T13:48:25.9983475Z 
2024-01-13T13:48:25.9983912Z #22 [stage-0 12/12] RUN npm run build
2024-01-13T13:48:26.4505570Z #22 0.484 
2024-01-13T13:48:26.4506329Z #22 0.484 > skellybot@0.0.1 build
2024-01-13T13:48:26.4507048Z #22 0.484 > nest build
2024-01-13T13:48:26.4507824Z #22 0.484 
2024-01-13T13:48:31.1088063Z #22 5.136 npm notice 
2024-01-13T13:48:31.1089586Z #22 5.136 npm notice New minor version of npm available! 10.2.3 -> 10.3.0
2024-01-13T13:48:31.1091217Z #22 5.136 npm notice Changelog: <https://github.com/npm/cli/releases/tag/v10.3.0>
2024-01-13T13:48:31.1092618Z #22 5.136 npm notice Run `npm install -g npm@10.3.0` to update!
2024-01-13T13:48:31.1093472Z #22 5.137 npm notice 
2024-01-13T13:48:31.2598950Z #22 DONE 5.3s
2024-01-13T13:48:31.2599449Z 
2024-01-13T13:48:31.2599694Z #23 exporting to image
2024-01-13T13:48:31.2600358Z #23 exporting layers
2024-01-13T13:48:37.7799142Z #23 exporting layers 6.6s done
2024-01-13T13:48:37.7800228Z #23 writing image sha256:ce5588e625378d80e8176f0698ffb45a2e85e73a4c1bf003f0ba92299e99cb22 done
2024-01-13T13:48:37.7801853Z #23 naming to us-east1-docker.pkg.dev/mocap-test-project/jonbot/nestbot:042e1b9eee40ab55edabb9a9e4e8f6d36b3f6da0 done
2024-01-13T13:48:37.7802739Z #23 DONE 6.6s
2024-01-13T13:48:38.0453482Z #0 building with "default" instance using docker driver
2024-01-13T13:48:38.0454267Z 
2024-01-13T13:48:38.0454632Z #1 [internal] load build definition from Dockerfile
2024-01-13T13:48:38.0455532Z #1 transferring dockerfile: 1.03kB done
2024-01-13T13:48:38.0456482Z #1 DONE 0.0s
2024-01-13T13:48:38.0456858Z 
2024-01-13T13:48:38.0457149Z #2 [internal] load .dockerignore
2024-01-13T13:48:38.0458672Z #2 transferring context: 57B done
2024-01-13T13:48:38.0459487Z #2 DONE 0.0s
2024-01-13T13:48:38.0459869Z 
2024-01-13T13:48:38.0460301Z #3 resolve image config for docker.io/docker/dockerfile:1.2
2024-01-13T13:48:38.0461309Z #3 DONE 0.1s
2024-01-13T13:48:38.0461691Z 
2024-01-13T13:48:38.0463145Z #4 docker-image://docker.io/docker/dockerfile:1.2@sha256:e2a8561e419ab1ba6b2fe6cbdf49fd92b95912df1cf7d313c3e2230a333fdbcc
2024-01-13T13:48:38.0464585Z #4 CACHED
2024-01-13T13:48:38.1522650Z 
2024-01-13T13:48:38.1523542Z #5 [internal] load .dockerignore
2024-01-13T13:48:38.1524081Z #5 DONE 0.0s
2024-01-13T13:48:38.1524467Z 
2024-01-13T13:48:38.1524713Z #6 [internal] load build definition from Dockerfile
2024-01-13T13:48:38.1525194Z #6 DONE 0.0s
2024-01-13T13:48:38.1525399Z 
2024-01-13T13:48:38.1525988Z #7 [internal] load metadata for docker.io/library/node:20.10.0-slim
2024-01-13T13:48:38.1526536Z #7 DONE 0.1s
2024-01-13T13:48:38.1526712Z 
2024-01-13T13:48:38.1527664Z #8 [stage-0  1/12] FROM docker.io/library/node:20.10.0-slim@sha256:5c714c3e90f66a2cbfa266b90a4d7adcd63453cd730aa2d13cba84b260bea2e6
2024-01-13T13:48:38.1529006Z #8 DONE 0.0s
2024-01-13T13:48:38.1529191Z 
2024-01-13T13:48:38.1529695Z #9 [internal] load build context
2024-01-13T13:48:38.1530168Z #9 transferring context: 14.69kB 0.0s done
2024-01-13T13:48:38.1682515Z #9 DONE 0.0s
2024-01-13T13:48:38.1682909Z 
2024-01-13T13:48:38.1683539Z #10 [stage-0  3/12] RUN rm -rf /etc/apt/apt.conf.d/docker-clean
2024-01-13T13:48:38.1684621Z #10 CACHED
2024-01-13T13:48:38.1684977Z 
2024-01-13T13:48:38.1685613Z #11 [stage-0 10/12] RUN --mount=type=cache,target=/root/.cache npm ci
2024-01-13T13:48:38.1686698Z #11 CACHED
2024-01-13T13:48:38.1687154Z 
2024-01-13T13:48:38.1687439Z #12 [stage-0 11/12] COPY . .
2024-01-13T13:48:38.1688054Z #12 CACHED
2024-01-13T13:48:38.1688366Z 
2024-01-13T13:48:38.1689233Z #13 [stage-0  6/12] RUN useradd -m appuser && chown -R appuser /workspace && chown -R appuser "/home/.npm"
2024-01-13T13:48:38.1690582Z #13 CACHED
2024-01-13T13:48:38.1690886Z 
2024-01-13T13:48:38.1691285Z #14 [stage-0  8/12] COPY package-lock.json .
2024-01-13T13:48:38.1692145Z #14 CACHED
2024-01-13T13:48:38.1692412Z 
2024-01-13T13:48:38.1692776Z #15 [stage-0  9/12] COPY package.json .
2024-01-13T13:48:38.1693508Z #15 CACHED
2024-01-13T13:48:38.1693862Z 
2024-01-13T13:48:38.1694211Z #16 [stage-0  2/12] WORKDIR /workspace
2024-01-13T13:48:38.1694891Z #16 CACHED
2024-01-13T13:48:38.1695174Z 
2024-01-13T13:48:38.1696441Z #17 [stage-0  7/12] RUN --mount=type=cache,target=/var/cache/apt ./install_packages     dumb-init     htop     make     g++     python3
2024-01-13T13:48:38.1698811Z #17 CACHED
2024-01-13T13:48:38.1699089Z 
2024-01-13T13:48:38.1699485Z #18 [stage-0  5/12] RUN mkdir /home/.npm
2024-01-13T13:48:38.1700283Z #18 CACHED
2024-01-13T13:48:38.1700579Z 
2024-01-13T13:48:38.1700933Z #19 [stage-0  4/12] COPY ./bin/builds/ .
2024-01-13T13:48:38.1701625Z #19 CACHED
2024-01-13T13:48:38.1701972Z 
2024-01-13T13:48:38.1702334Z #20 [stage-0 12/12] RUN npm run build
2024-01-13T13:48:38.1703030Z #20 CACHED
2024-01-13T13:48:38.1703282Z 
2024-01-13T13:48:38.1703623Z #21 exporting to image
2024-01-13T13:48:38.1704210Z #21 exporting layers done
2024-01-13T13:48:38.1705271Z #21 writing image sha256:ce5588e625378d80e8176f0698ffb45a2e85e73a4c1bf003f0ba92299e99cb22 done
2024-01-13T13:48:38.1706925Z #21 naming to us-east1-docker.pkg.dev/mocap-test-project/jonbot/nestbot:latest done
2024-01-13T13:48:38.1707924Z #21 DONE 0.0s
2024-01-13T13:48:38.1867509Z The push refers to repository [us-east1-docker.pkg.dev/mocap-test-project/jonbot/nestbot]
2024-01-13T13:48:38.2298505Z 0c476f4f690e: Preparing
2024-01-13T13:48:38.2300455Z 0d61503ed644: Preparing
2024-01-13T13:48:38.2301161Z 837be668e4b4: Preparing
2024-01-13T13:48:38.2301702Z a514ad249fbe: Preparing
2024-01-13T13:48:38.2302098Z 1574dfe03b80: Preparing
2024-01-13T13:48:38.2302491Z 50ef1083e44d: Preparing
2024-01-13T13:48:38.2302925Z 110362366c09: Preparing
2024-01-13T13:48:38.2303307Z 1a3b402dc68e: Preparing
2024-01-13T13:48:38.2303748Z 2f02c0fb7600: Preparing
2024-01-13T13:48:38.2304111Z ca994a0490b8: Preparing
2024-01-13T13:48:38.2304486Z bcf0151c0d41: Preparing
2024-01-13T13:48:38.2304910Z 54670042a040: Preparing
2024-01-13T13:48:38.2305292Z 0d1064329154: Preparing
2024-01-13T13:48:38.2305654Z e15f668bdea1: Preparing
2024-01-13T13:48:38.2306082Z 6a02db9fb904: Preparing
2024-01-13T13:48:38.2306462Z 7292cf786aa8: Preparing
2024-01-13T13:48:38.2306877Z 110362366c09: Waiting
2024-01-13T13:48:38.2307248Z 1a3b402dc68e: Waiting
2024-01-13T13:48:38.2307596Z 2f02c0fb7600: Waiting
2024-01-13T13:48:38.2308004Z ca994a0490b8: Waiting
2024-01-13T13:48:38.2308358Z bcf0151c0d41: Waiting
2024-01-13T13:48:38.2308701Z 54670042a040: Waiting
2024-01-13T13:48:38.2309117Z 0d1064329154: Waiting
2024-01-13T13:48:38.2309456Z e15f668bdea1: Waiting
2024-01-13T13:48:38.2309862Z 6a02db9fb904: Waiting
2024-01-13T13:48:38.2310223Z 7292cf786aa8: Waiting
2024-01-13T13:48:38.2310561Z 50ef1083e44d: Waiting
2024-01-13T13:48:38.9721784Z a514ad249fbe: Pushed
2024-01-13T13:48:38.9793227Z 1574dfe03b80: Pushed
2024-01-13T13:48:38.9929380Z 0c476f4f690e: Pushed
2024-01-13T13:48:39.5251148Z 110362366c09: Pushed
2024-01-13T13:48:39.6104459Z 1a3b402dc68e: Pushed
2024-01-13T13:48:39.6594986Z 0d61503ed644: Pushed
2024-01-13T13:48:40.1357180Z 2f02c0fb7600: Pushed
2024-01-13T13:48:40.2125352Z bcf0151c0d41: Pushed
2024-01-13T13:48:40.2531029Z 54670042a040: Layer already exists
2024-01-13T13:48:40.2791200Z ca994a0490b8: Pushed
2024-01-13T13:48:40.3388754Z 0d1064329154: Layer already exists
2024-01-13T13:48:40.3715098Z e15f668bdea1: Layer already exists
2024-01-13T13:48:40.4011053Z 6a02db9fb904: Layer already exists
2024-01-13T13:48:40.4779535Z 7292cf786aa8: Layer already exists
2024-01-13T13:48:51.6465093Z 50ef1083e44d: Pushed
2024-01-13T13:48:52.3813886Z 837be668e4b4: Pushed
2024-01-13T13:48:53.2495769Z 042e1b9eee40ab55edabb9a9e4e8f6d36b3f6da0: digest: sha256:0eb25da4984de943a4f01ee980d8ece7b3289a92de1deba15b14e714e3b32a17 size: 3666
2024-01-13T13:48:53.2657124Z The push refers to repository [us-east1-docker.pkg.dev/mocap-test-project/jonbot/nestbot]
2024-01-13T13:48:53.3048077Z 0c476f4f690e: Preparing
2024-01-13T13:48:53.3048961Z 0d61503ed644: Preparing
2024-01-13T13:48:53.3049612Z 837be668e4b4: Preparing
2024-01-13T13:48:53.3050210Z a514ad249fbe: Preparing
2024-01-13T13:48:53.3050881Z 1574dfe03b80: Preparing
2024-01-13T13:48:53.3051440Z 50ef1083e44d: Preparing
2024-01-13T13:48:53.3052134Z 110362366c09: Preparing
2024-01-13T13:48:53.3052695Z 1a3b402dc68e: Preparing
2024-01-13T13:48:53.3053283Z 2f02c0fb7600: Preparing
2024-01-13T13:48:53.3053932Z ca994a0490b8: Preparing
2024-01-13T13:48:53.3054498Z bcf0151c0d41: Preparing
2024-01-13T13:48:53.3055104Z 54670042a040: Preparing
2024-01-13T13:48:53.3055741Z 0d1064329154: Preparing
2024-01-13T13:48:53.3056320Z e15f668bdea1: Preparing
2024-01-13T13:48:53.3056974Z 6a02db9fb904: Preparing
2024-01-13T13:48:53.3057731Z 7292cf786aa8: Preparing
2024-01-13T13:48:53.3058334Z 50ef1083e44d: Waiting
2024-01-13T13:48:53.3058916Z 110362366c09: Waiting
2024-01-13T13:48:53.3059297Z 1a3b402dc68e: Waiting
2024-01-13T13:48:53.3059647Z 2f02c0fb7600: Waiting
2024-01-13T13:48:53.3060060Z ca994a0490b8: Waiting
2024-01-13T13:48:53.3060430Z bcf0151c0d41: Waiting
2024-01-13T13:48:53.3060849Z 54670042a040: Waiting
2024-01-13T13:48:53.3061206Z 0d1064329154: Waiting
2024-01-13T13:48:53.3061546Z e15f668bdea1: Waiting
2024-01-13T13:48:53.3061952Z 6a02db9fb904: Waiting
2024-01-13T13:48:53.3062303Z 7292cf786aa8: Waiting
2024-01-13T13:48:53.4202375Z 0d61503ed644: Layer already exists
2024-01-13T13:48:53.4203460Z 0c476f4f690e: Layer already exists
2024-01-13T13:48:53.4322662Z a514ad249fbe: Layer already exists
2024-01-13T13:48:53.4367047Z 1574dfe03b80: Layer already exists
2024-01-13T13:48:53.4387654Z 837be668e4b4: Layer already exists
2024-01-13T13:48:53.4797804Z 110362366c09: Layer already exists
2024-01-13T13:48:53.5020610Z 2f02c0fb7600: Layer already exists
2024-01-13T13:48:53.5068614Z ca994a0490b8: Layer already exists
2024-01-13T13:48:53.5425363Z 50ef1083e44d: Layer already exists
2024-01-13T13:48:53.5495516Z bcf0151c0d41: Layer already exists
2024-01-13T13:48:53.5603938Z 1a3b402dc68e: Layer already exists
2024-01-13T13:48:53.5610461Z 0d1064329154: Layer already exists
2024-01-13T13:48:53.5768413Z 54670042a040: Layer already exists
2024-01-13T13:48:53.6058090Z e15f668bdea1: Layer already exists
2024-01-13T13:48:53.6120045Z 6a02db9fb904: Layer already exists
2024-01-13T13:48:53.6229887Z 7292cf786aa8: Layer already exists
2024-01-13T13:48:53.9416907Z latest: digest: sha256:0eb25da4984de943a4f01ee980d8ece7b3289a92de1deba15b14e714e3b32a17 size: 3666
2024-01-13T13:48:53.9473295Z ##[group]Run gcloud compute instances stop skelly-bot-testing --zone=us-central1-a
2024-01-13T13:48:53.9474256Z [36;1mgcloud compute instances stop skelly-bot-testing --zone=us-central1-a[0m
2024-01-13T13:48:53.9475157Z [36;1mgcloud compute instances start skelly-bot-testing --zone=us-central1-a[0m
2024-01-13T13:48:53.9525478Z shell: /usr/bin/bash -e {0}
2024-01-13T13:48:53.9525894Z env:
2024-01-13T13:48:53.9526233Z   PROJECT_ID: mocap-test-project
2024-01-13T13:48:53.9526778Z   GAR_LOCATION: us-east1
2024-01-13T13:48:53.9527157Z   SERVICE: jonbot/nestbot
2024-01-13T13:48:53.9527599Z   REGION: us-central1
2024-01-13T13:48:53.9528304Z   CLOUDSDK_AUTH_CREDENTIAL_FILE_OVERRIDE: /home/runner/work/skellybot/skellybot/gha-creds-51ca75be46286648.json
2024-01-13T13:48:53.9529332Z   GOOGLE_APPLICATION_CREDENTIALS: /home/runner/work/skellybot/skellybot/gha-creds-51ca75be46286648.json
2024-01-13T13:48:53.9530471Z   GOOGLE_GHA_CREDS_PATH: /home/runner/work/skellybot/skellybot/gha-creds-51ca75be46286648.json
2024-01-13T13:48:53.9531175Z   CLOUDSDK_CORE_PROJECT: mocap-test-project
2024-01-13T13:48:53.9531723Z   CLOUDSDK_PROJECT: mocap-test-project
2024-01-13T13:48:53.9532170Z   GCLOUD_PROJECT: mocap-test-project
2024-01-13T13:48:53.9532640Z   GCP_PROJECT: mocap-test-project
2024-01-13T13:48:53.9533164Z   GOOGLE_CLOUD_PROJECT: mocap-test-project
2024-01-13T13:48:53.9533600Z ##[endgroup]
2024-01-13T13:49:00.0122201Z Stopping instance(s) skelly-bot-testing...
2024-01-13T13:49:21.3324095Z ..........................................................................................................done.
2024-01-13T13:49:21.4268337Z Updated [https://compute.googleapis.com/compute/v1/projects/mocap-test-project/zones/us-central1-a/instances/skelly-bot-testing].
2024-01-13T13:49:23.0141743Z Starting instance(s) skelly-bot-testing...
2024-01-13T13:49:31.9158802Z ............................................done.
2024-01-13T13:49:32.1967529Z Updated [https://compute.googleapis.com/compute/v1/projects/mocap-test-project/zones/us-central1-a/instances/skelly-bot-testing].
2024-01-13T13:49:32.1968880Z Instance internal IP is 10.128.0.10
2024-01-13T13:49:32.1969603Z Instance external IP is 35.208.74.176
2024-01-13T13:49:32.3287884Z ##[group]Run echo 
2024-01-13T13:49:32.3288494Z [36;1mecho [0m
2024-01-13T13:49:32.3338571Z shell: /usr/bin/bash -e {0}
2024-01-13T13:49:32.3339005Z env:
2024-01-13T13:49:32.3339343Z   PROJECT_ID: mocap-test-project
2024-01-13T13:49:32.3339833Z   GAR_LOCATION: us-east1
2024-01-13T13:49:32.3340246Z   SERVICE: jonbot/nestbot
2024-01-13T13:49:32.3340685Z   REGION: us-central1
2024-01-13T13:49:32.3341398Z   CLOUDSDK_AUTH_CREDENTIAL_FILE_OVERRIDE: /home/runner/work/skellybot/skellybot/gha-creds-51ca75be46286648.json
2024-01-13T13:49:32.3342436Z   GOOGLE_APPLICATION_CREDENTIALS: /home/runner/work/skellybot/skellybot/gha-creds-51ca75be46286648.json
2024-01-13T13:49:32.3343429Z   GOOGLE_GHA_CREDS_PATH: /home/runner/work/skellybot/skellybot/gha-creds-51ca75be46286648.json
2024-01-13T13:49:32.3344140Z   CLOUDSDK_CORE_PROJECT: mocap-test-project
2024-01-13T13:49:32.3344830Z   CLOUDSDK_PROJECT: mocap-test-project
2024-01-13T13:49:32.3345379Z   GCLOUD_PROJECT: mocap-test-project
2024-01-13T13:49:32.3345910Z   GCP_PROJECT: mocap-test-project
2024-01-13T13:49:32.3346453Z   GOOGLE_CLOUD_PROJECT: mocap-test-project
2024-01-13T13:49:32.3346885Z ##[endgroup]
2024-01-13T13:49:32.3417445Z 
2024-01-13T13:49:32.3466410Z Post job cleanup.
2024-01-13T13:49:32.4491213Z [command]/usr/bin/docker logout us-east1-docker.pkg.dev
2024-01-13T13:49:32.4630070Z Removing login credentials for us-east1-docker.pkg.dev
2024-01-13T13:49:32.4781577Z Post job cleanup.
2024-01-13T13:49:32.5600865Z Removed exported credentials at "/home/runner/work/skellybot/skellybot/gha-creds-51ca75be46286648.json".
2024-01-13T13:49:32.5722949Z Post job cleanup.
2024-01-13T13:49:32.6465246Z [command]/usr/bin/git version
2024-01-13T13:49:32.6507191Z git version 2.43.0
2024-01-13T13:49:32.6554930Z Temporarily overriding HOME='/home/runner/work/_temp/9925e3f3-b557-43e6-ba79-16ab60c19787' before making global git config changes
2024-01-13T13:49:32.6556163Z Adding repository directory to the temporary git global config as a safe directory
2024-01-13T13:49:32.6560641Z [command]/usr/bin/git config --global --add safe.directory /home/runner/work/skellybot/skellybot
2024-01-13T13:49:32.6595055Z [command]/usr/bin/git config --local --name-only --get-regexp core\.sshCommand
2024-01-13T13:49:32.6626931Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"
2024-01-13T13:49:32.6865963Z [command]/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
2024-01-13T13:49:32.6886100Z http.https://github.com/.extraheader
2024-01-13T13:49:32.6897847Z [command]/usr/bin/git config --local --unset-all http.https://github.com/.extraheader
2024-01-13T13:49:32.6928786Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :"
2024-01-13T13:49:32.7395817Z Cleaning up orphan processes



LOGS FROM A NON-WORKING BROKEN DEPLOYMENT END
=======================




