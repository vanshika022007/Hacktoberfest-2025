import os
import shutil
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from file_organizer import organize_files

TEST_DIR = 'test_folder'
TXT_FILE = 'test.txt'
PNG_FILE = 'test.png'
NOEXT_FILE = 'noextfile'


def setup_module():
    """
    Create a directory with test files automagically before testing
    """
    os.makedirs(TEST_DIR, exist_ok=True)
    open(os.path.join(TEST_DIR, TXT_FILE), 'w').close()
    open(os.path.join(TEST_DIR, PNG_FILE), 'w').close()
    open(os.path.join(TEST_DIR, NOEXT_FILE), 'w').close()


def teardown_module():
    """
    Delete the test directory and its contents automagically after testing
    """
    if os.path.exists(TEST_DIR):
        shutil.rmtree(TEST_DIR, ignore_errors=True)


def test_create_folder():
    # Interestingly, if organize_files is not called, the folders are not created (setup_module is not called)
    organize_files(TEST_DIR, log_activity=False)

    # Check if the folders were created
    assert os.path.isdir(os.path.join(TEST_DIR, 'txt'))
    assert os.path.isdir(os.path.join(TEST_DIR, 'png'))
    assert os.path.isdir(os.path.join(TEST_DIR, 'no_extension'))


def test_organize_files():
    organize_files(TEST_DIR, log_activity=False)

    # Check if files were MOVED to their respective folders
    assert os.path.exists(os.path.join(TEST_DIR, 'txt', TXT_FILE))
    assert os.path.exists(os.path.join(TEST_DIR, 'png', PNG_FILE))
    assert os.path.exists(os.path.join(TEST_DIR, 'no_extension', NOEXT_FILE))

    # Check if original files were DELETED
    assert not os.path.exists(os.path.join(TEST_DIR, TXT_FILE))
    assert not os.path.exists(os.path.join(TEST_DIR, PNG_FILE))
    assert not os.path.exists(os.path.join(TEST_DIR, NOEXT_FILE))


def test_log_activity(tmpdir):
    folder_path = tmpdir.mkdir("tmp_folder")
    (folder_path / "test_file.txt").write("")

    organize_files(str(folder_path), log_activity=True)

    # Check if the log file was created
    log_path = os.path.join(str(folder_path), "organizer_log.txt")
    assert os.path.exists(log_path)

    # Check if the log file contains the expected content
    with open(log_path, 'r') as f:
        content = f.read()
        assert "Moved: test_file.txt" in content


def test_logfile_does_not_exist(tmpdir):
    folder_path = tmpdir.mkdir("tmp_folder")
    (folder_path / "test_file.txt").write("")

    organize_files(str(folder_path), log_activity=False)
    # Check if the log file was not created
    log_path = os.path.join(str(folder_path), "organizer_log.txt")
    assert not os.path.exists(log_path)


def test_organize_files_nonexistent_folder(capfd):
    organize_files('/invalid/path', log_activity=False)

    # Standard output
    captured = capfd.readouterr()

    assert '❌ The specified folder does not exist.' in captured.out


def test_organize_files_skips_directories(tmp_path):
    temp_folder_path = tmp_path / 'test_folder'
    temp_folder_path.mkdir()

    # Create a subfolder
    subfolder_path = temp_folder_path / 'subfolder'
    subfolder_path.mkdir()

    # Check if the subfolder is created
    assert subfolder_path.exists()
    assert subfolder_path.is_dir()

    organize_files(str(temp_folder_path), log_activity=False)

    # Check if the subfolder is still there after organizing
    assert subfolder_path.exists()
    assert subfolder_path.is_dir()

    assert os.path.exists(os.path.join(temp_folder_path, 'subfolder'))


def test_organize_files_outputs_summary(capfd, tmpdir):

    # Create a temporary folder
    folder_path = tmpdir.mkdir("tmp_folder")
    (folder_path / "file1.txt").write("")
    (folder_path / "file2.png").write("")

    organize_files(str(folder_path), log_activity=False)

    captured = capfd.readouterr()
    assert "✅ Organized 2 files by extension." in captured.out
