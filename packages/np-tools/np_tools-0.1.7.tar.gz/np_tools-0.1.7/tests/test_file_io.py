import np_logging

from np_tools import *

def test_copy_dir_to_dir(tmp_path):
    src = tmp_path / 'src'
    dest = tmp_path / 'dest'
    src.mkdir()
    (src / 'test.txt').write_text('hello world')
    copy(src, dest)
    assert (dest / 'test.txt').exists()
    assert (dest / 'test.txt').read_text() == 'hello world'

def test_copy_new_file_to_dir(tmp_path):
    src = tmp_path / 'src'
    dest = tmp_path / 'dest'
    src.mkdir()
    (src / 'test.txt').write_text('hello world')
    copy(src / 'test.txt', dest)
    assert (dest / 'test.txt').exists()
    assert (dest / 'test.txt').read_text() == 'hello world'

def test_copy_new_file_to_file(tmp_path):
    src = tmp_path / 'src'
    dest = tmp_path / 'dest'
    src.mkdir()
    (src / 'test.txt').write_text('hello world')
    copy(src / 'test.txt', dest / 'test.txt')
    assert (dest / 'test.txt').exists()
    assert (dest / 'test.txt').read_text() == 'hello world'


def test_copy_new_dir(tmp_path):
    src = tmp_path / 'src'
    dest = tmp_path / 'dest'
    src.mkdir()
    (src / 'test.txt').write_text('hello world')
    copy(src, dest)
    assert (dest).exists()
    assert (dest / 'test.txt').exists()
    assert (dest / 'test.txt').read_text() == 'hello world'
    
    
def test_validate_existing_file(tmp_path):
    src = tmp_path / 'src'
    dest = tmp_path / 'dest'
    src.mkdir()
    dest.mkdir()
    (src / 'test.txt').write_text('hello world')
    (dest / 'test.txt').write_text('_')
    copy(src / 'test.txt', dest)
    assert (dest / 'test.txt').read_text() == 'hello world'
    
def test_validate_existing_dir(tmp_path):
    src = tmp_path / 'src'
    dest = tmp_path / 'dest'
    src.mkdir()
    dest.mkdir()
    (src / 'test.txt').write_text('hello world')
    (dest / 'test.txt').write_text('_')
    copy(src, dest)
    assert (dest / 'test.txt').read_text() == 'hello world'
    
def test_validate_move_dir(tmp_path):
    src = tmp_path / 'src'
    dest = tmp_path / 'dest'
    src.mkdir()
    dest.mkdir()
    (src / 'test.txt').write_text('hello world')
    (dest / 'test.txt').write_text('_')
    move(src, dest)
    assert (dest / 'test.txt').read_text() == 'hello world'
    assert not src.exists()
    
def test_validate_move_file(tmp_path):
    src = tmp_path / 'src'
    dest = tmp_path / 'dest'
    src.mkdir()
    dest.mkdir()
    (src / 'test.txt').write_text('hello world')
    (dest / 'test.txt').write_text('_')
    move(src / 'test.txt', dest)
    assert (dest / 'test.txt').read_text() == 'hello world'
    assert src.exists()
    assert not (src / 'test.txt').exists()