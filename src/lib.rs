use convert_case::{Case, Casing};
use pyo3::prelude::*;

/// Convert to camel case.
#[pyfunction]
fn to_camel(s: String) -> PyResult<String> {
    Ok(s.to_case(Case::Camel))
}

/// Convert from snake to camel case.
#[pyfunction]
fn snake_to_camel(s: String) -> PyResult<String> {
    Ok(s.from_case(Case::Snake).to_case(Case::Camel))
}

/// Casers package.
#[pymodule]
fn _casers(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(to_camel, m)?)?;
    m.add_function(wrap_pyfunction!(snake_to_camel, m)?)?;
    Ok(())
}
