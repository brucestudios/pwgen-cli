use assert_cmd::Command;
use predicates::prelude::*;

#[test]
fn test_default_uniform() -> Result<(), Box<dyn std::error::Error>> {
    let mut cmd = Command::cargo_bin("randgen")?;
    cmd.arg("--count").arg("3");
    cmd.assert()
        .success()
        .stdout(predicate::str::matches(r"^[\d\.]+(\s[\d\.]+){2}$").expect("regex error"));
    Ok(())
}

#[test]
fn test_normal_distribution() -> Result<(), Box<dyn std::error::Error>> {
    let mut cmd = Command::cargo_bin("randgen")?;
    cmd.arg("--normal")
        .arg("--mean").arg("5.0")
        .arg("--stddev").arg("2.0")
        .arg("--count").arg("2");
    cmd.assert()
        .success()
        .stdout(predicate::str::matches(r"^[\d\.\-eE]+(\s[\d\.\-eE]+){1}$").expect("regex error"));
    Ok(())
}

#[test]
fn test_exponential_distribution() -> Result<(), Box<dyn std::error::Error>> {
    let mut cmd = Command::cargo_bin("randgen")?;
    cmd.arg("--exponential")
        .arg("--lambda").arg("0.5")
        .arg("--count").arg("2");
    cmd.assert()
        .success()
        .stdout(predicate::str::matches(r"^[\d\.]+(\s[\d\.]+){1}$").expect("regex error"));
    Ok(())
}

#[test]
fn test_poisson_distribution() -> Result<(), Box<dyn std::error::Error>> {
    let mut cmd = Command::cargo_bin("randgen")?;
    cmd.arg("--poisson")
        .arg("--lambda").arg("3.0")
        .arg("--count").arg("2");
    cmd.assert()
        .success()
        .stdout(predicate::str::matches(r"^\d+(\s\d+){1}$").expect("regex error"));
    Ok(())
}

#[test]
fn test_space_separated_format() -> Result<(), Box<dyn std::error::Error>> {
    let mut cmd = Command::cargo_bin("randgen")?;
    cmd.arg("--count").arg("2")
        .arg("--format").arg("space-separated");
    cmd.assert()
        .success()
        .stdout(predicate::str::matches(r"^[\d\.]+(\s[\d\.]+){1}$").expect("regex error"));
    Ok(())
}

#[test]
fn test_one_per_line_format() -> Result<(), Box<dyn std::error::Error>> {
    let mut cmd = Command::cargo_bin("randgen")?;
    cmd.arg("--count").arg("2")
        .arg("--format").arg("one-per-line");
    cmd.assert()
        .success()
        .stdout(predicate::str::matches(r"^[\d\.]+\n[\d\.]+$").expect("regex error"));
    Ok(())
}