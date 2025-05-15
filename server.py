from mcp.server.fastmcp import FastMCP,Context
import os
import sys
import distro
import subprocess
mcp = FastMCP("arch-system-manager")

@mcp.tool(description="Update system")
async def update_system()->str:
    print("Checking platform...",file=sys.stderr)
    distribution_name = distro.name()
    if distribution_name.find("Arch")!=-1:
        print("Checking updates...,file=sys.stderr)")
        process = subprocess.run("pkexec sudo pacman -Syu --noconfirm".split(),stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        errors = process.stderr
        if errors:
            errors =errors.decode()
            print(errors,file=sys.stderr)
        prompt = process.stdout
        if prompt:
            prompt = prompt.decode()
            if prompt.find("今日无事可做")!=-1 or prompt.find("Nothing to do")!=-1:
                return "System is up to date."
        
        return "System updated successfully."

    else:
        return f"linux {distribution_name} is not supported platform."

@mcp.tool(description="Install package")
async def install_package(package:str)->str:
    print("Checking platform...",file=sys.stderr)
    distribution_name = distro.name()
    if distribution_name.find("Arch")!=-1:
        print("Installing package...",file=sys.stderr)
        process = subprocess.run(f"pkexec sudo pacman -S {package} --noconfirm".split(),stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        errors = process.stderr
        if errors:
            errors =errors.decode()
            print(errors,file=sys.stderr)
        prompt = process.stdout
        if prompt:
            prompt = prompt.decode()
            return prompt

        return f"{package} installed successfully."

    else:
        return f"linux {distribution_name} is not supported platform."

@mcp.tool(description="Uninstall package")
async def uninstall_package(package:str)->str:
    print("Checking platform...",file=sys.stderr)
    distribution_name = distro.name()
    if distribution_name.find("Arch")!=-1:
        print("Uninstalling package...",file=sys.stderr)
        process = subprocess.run(f"pkexec sudo pacman -R {package} --noconfirm".split(),stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        errors = process.stderr
        if errors:
            errors =errors.decode()
            print(errors,file=sys.stderr)
        prompt = process.stdout
        if prompt:
            prompt = prompt.decode()
            return prompt

        return f"{package} uninstalled successfully."

    else:
        return f"linux {distribution_name} is not supported platform."

@mcp.tool(description="Check package")
async def check_package(package:str)->str:
    print("Checking platform...",file=sys.stderr)
    distribution_name = distro.name()
    if distribution_name.find("Arch")!=-1:
        print("Checking package...",file=sys.stderr)
        process = subprocess.run(f"pkexec sudo pacman -Q {package}".split(),stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        errors = process.stderr
        if errors:
            errors =errors.decode()
            return errors
        prompt = process.stdout
        if prompt:
            prompt = prompt.decode()
            return prompt

        return f"{package} is not installed."

    else:
        return f"linux {distribution_name} is not supported platform."

@mcp.tool(description="Remove orphan package")
async def remove_orphan_package()->str:
    print("Checking platform...",file=sys.stderr)
    distribution_name = distro.name()
    if distribution_name.find("Arch")!=-1:
        print("Removing orphan package...",file=sys.stderr)
        process = subprocess.run(f"pkexec sudo pacman -Rns $(pacman -Qdtq) --noconfirm".split(),stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        errors = process.stderr
        if errors:
            errors =errors.decode()
            print(errors,file=sys.stderr)
        prompt = process.stdout
        if prompt:
            prompt = prompt.decode()
            return prompt

        return f"Orphan packages removed successfully."

    else:
        return f"linux {distribution_name} is not supported platform."

@mcp.tool(description="Manage service")
async def manage_service(service:str,action:str)->str:
    print("Checking platform...",file=sys.stderr)
    distribution_name = distro.name()
    if distribution_name.find("Arch")!=-1:
        print("Managing service...",file=sys.stderr)
        process = subprocess.run(f"pkexec sudo systemctl {action} {service}".split(),stderr=subprocess.PIPE,stdout=subprocess.PIPE)
        errors = process.stderr
        if errors:
            errors =errors.decode()
            return
        prompt = process.stdout
        if prompt:
            prompt = prompt.decode()
            return prompt

        return f"{service} {action} successfully."

    else:
        return f"linux {distribution_name} is not supported platform."

@mcp.tool(description="Check service status")
async def check_service_status(service:str)->str:
    print("Checking platform...",file=sys.stderr)
    distribution_name = distro.name()
    if distribution_name.find("Arch")!=-1:
        print("Checking service status...",file=sys.stderr)
        process = subprocess.run(f"pkexec sudo systemctl status {service}".split(),stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        errors = process.stderr
        if errors:
            errors =errors.decode()
            return errors
        prompt = process.stdout
        if prompt:
            prompt = prompt.decode()
            return prompt

        return f"{service} is not installed."

    else:
        return f"linux {distribution_name} is not supported platform."
    
@mcp.tool(description="add locale")
async def add_locale(locale:str)->str:
    print("Checking platform...",file=sys.stderr)
    distribution_name = distro.name()
    if distribution_name.find("Arch")!=-1:
        print("Adding locale...",file=sys.stderr)
        process = subprocess.run(f"pkexec sudo localectl set-locale {locale}".split(),stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        errors = process.stderr
        if errors:
            errors =errors.decode()
            print(errors,file=sys.stderr)
        prompt = process.stdout
        if prompt:
            prompt = prompt.decode()
            return prompt

        return f"{locale} added successfully."

    else:
        return f"linux {distribution_name} is not supported platform."
    
@mcp.tool(description="sync system time")
async def sync_system_time()->str:
    print("Checking platform...",file=sys.stderr)
    distribution_name = distro.name()
    if distribution_name.find("Arch")!=-1:
        print("Syncing system time...",file=sys.stderr)
        process = subprocess.run(f"pkexec sudo timedatectl set-ntp true".split(),stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        errors = process.stderr
        if errors:
            errors =errors.decode()
            print(errors,file=sys.stderr)
        prompt = process.stdout
        if prompt:
            prompt = prompt.decode()
            return prompt

        return f"System time synced successfully."

    else:
        return f"linux {distribution_name} is not supported platform."


@mcp.tool(description="Add user")
async def add_user(username:str,password:str,groups:str,shell:str,home:str,email:str)->str:
    print("Checking platform...",file=sys.stderr)
    distribution_name = distro.name()
    if distribution_name.find("Arch")!=-1:
        print("Adding user...",file=sys.stderr)
        process = subprocess.run(f"pkexec sudo useradd -m -p {password} -G {groups} -s {shell} -d {home} -e {email} {username}".split(),stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        errors = process.stderr
        if errors:
            errors =errors.decode()
            print(errors,file=sys.stderr)
        prompt = process.stdout
        if prompt:
            prompt = prompt.decode()
            return prompt

        return f"{username} added successfully."

    else:
        return f"linux {distribution_name} is not supported platform."

@mcp.tool(description="Delete user")
async def delete_user(username:str)->str:
    print("Checking platform...",file=sys.stderr)
    distribution_name = distro.name()
    if distribution_name.find("Arch")!=-1:
        print("Deleting user...",file=sys.stderr)
        process = subprocess.run(f"pkexec sudo userdel -r {username}".split(),stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        errors = process.stderr
        if errors:
            errors =errors.decode()
            print(errors,file=sys.stderr)
        prompt = process.stdout
        if prompt:
            prompt = prompt.decode()
            return prompt

        return f"{username} deleted successfully."

    else:
        return f"linux {distribution_name} is not supported platform."


if __name__=="__main__":
    mcp.run()