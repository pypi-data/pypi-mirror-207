
import setuptools

if __name__ == "__main__":
    setuptools.setup(
        name="certora-cli-alpha-yuvalbd-rule_events_error_checking_part_two",
        version="20230508.14.26.010376",
        author="Certora",
        author_email="support@certora.com",
        description="Runner for the Certora Prover",
        long_description="Commit 7472f07. Build and Run scripts for executing the Certora Prover on Solidity smart contracts.",
        long_description_content_type="text/markdown",
        url="https://pypi.org/project/certora-cli-alpha-yuvalbd-rule_events_error_checking_part_two",
        packages=setuptools.find_packages(),
        include_package_data=True,
        install_requires=['tabulate', 'requests', 'pycryptodome', 'tqdm', 'click', 'sly', 'argcomplete', 'json5'],
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        entry_points={
            "console_scripts": [
                "certoraRun = certora_cli.certoraRun:entry_point",
                "certoraMutate = certora_cli.certoraMutate:ext_gambit_entry_point"
            ]
        },
        python_requires='>=3.8.16',
    )
        