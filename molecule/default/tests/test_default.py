def test_files(host):
    files = [
        "/etc/resolv.conf",
    ]
    for file in files:
        f = host.file(file)
        assert f.exists
        assert f.is_file


def test_dns_search(host):
    resolv = host.file("/etc/resolv.conf")
    assert resolv.contains("example.com")
