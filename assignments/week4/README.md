# Week 4: Cloud VM Lifecycle Management & Multi-Cloud Automation

Contains Makefile automation scripts for provisioning, managing, and tearing down virtual machine lifecycles across local and multi-cloud environments

## Environments & Workflows

### 1. Assignment 4.1: Local Multipass Infrastructure [Makefile](assignments/week4/local/Makefile)
Manages local Ubuntu instances using Multipass
* **Launch:** `make launch`
* **Status:** `make status`
* **Stop:**  `make stop`
* **Clean:** `make clean`

### 2. Assignment 4.2: Jetstream2 OpenStack Cloud [Makefile.jetstream](assignments/week4/jetstream/Makefile.jetstream)
Automates cloud VM lifecycle on Jetstream2
* **Target Cloud:** `export OS_CLOUD=openstack`
* **Image / Flavor:** `Featured-Ubuntu22` / `m3.medium`
* **Launch:** `make -f Makefile.jetstream launch`
* **Status:** `make -f Makefile.jetstream status`
* **Stop:**  `make -f Makefile.jetstream stop`
* **Clean:** `make -f Makefile.jetstream clean`

### 3. Assignment 4.3: Chameleon Cloud KVM@TACC [Makefile.chameleon](assignments/week4/chameleon/Makefile.chameleon)
Automates cloud VM lifecycle on Chameleon Cloud 
* **Target Cloud:** `export OS_CLOUD=chameleon`
* **Image / Network:** `CC-Ubuntu22.04` / `sharednet1`
* **Flavor:** Project Lease Reservation ID (`reservation:c61813c3-961a-4d83-a464-4835edb7d33a`)
* **Launch:** `make -f Makefile.chameleon launch`
* **Status:** `make -f Makefile.chameleon status`
* **Stop:**  `make -f Makefile.chameleon stop`
* **Clean:** `make -f Makefile.chameleon clean`