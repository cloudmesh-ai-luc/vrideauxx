VM_NAME ?= devops-vm
IMAGE ?= 22.04
CPUS ?= 2
MEMORY ?= 2G
DISK ?= 10G

.PHONY: all launch status shell stop start delete clean help

all: launch

launch:
	@echo "Launching VM $(VM_NAME)..."
	multipass launch $(IMAGE) --name $(VM_NAME) --cpus $(CPUS) --memory $(MEMORY) --disk $(DISK)

status:
	multipass list

shell:
	multipass shell $(VM_NAME)

stop:
	multipass stop $(VM_NAME)

start:
	multipass start $(VM_NAME)

delete:
	multipass delete $(VM_NAME)
	multipass purge

clean: delete

help:
	@echo "Available targets:"
	@echo "  make launch  - Launch a new Multipass VM"
	@echo "  make status  - Show status of running VMs"
	@echo "  make shell   - Open interactive shell in the VM"
	@echo "  make stop    - Stop the VM"
	@echo "  make start   - Start the VM"
	@echo "  make clean   - Delete and purge the VM"
